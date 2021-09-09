from fastapi.encoders import jsonable_encoder

from app.db import crud
from app.db import schemas
from app.elasticseach.client import ElasticConnection

es = ElasticConnection("vehicles")


def create_vehicle(db, vehicle):
    result = crud.create(db, vehicle)
    if result:
        vehicle.marca = result.marca.marca

    es_indexing(result)
    return vehicle


def find_by_id(db, id):
    return crud.get_id(db, id)


def update_vehicle(vehicle_id, vehicle, db):
    result = crud.update(db, vehicle, vehicle_id)
    if result:
        vehicle.marca = result.marca.marca
    doc_id = es_search_id(vehicle_id, "_id")
    es_update_doc(doc_id, result)
    return vehicle


def patch_vehicle(vehicle_id, vehicle, db):
    stored_item_data = find_by_id(db, vehicle_id)
    stored_item_data = jsonable_encoder(stored_item_data)
    stored_item_model = schemas.VehicleUpdate(**stored_item_data)
    update_data = vehicle.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    return update_vehicle(vehicle_id, updated_item, db)


def get_all(db):
    result = crud.find_all(db)
    vehicles = list()
    for item in result:
        vehicle = build_vehicle(item)
        vehicles.append(vehicle)
    return vehicles


def delete(vehicle_id):
    result = f"{crud.remove(vehicle_id)} row deleted"
    query = {"query": {"match": {"id": f"{vehicle_id}"}}}
    es.delete(query)
    return result


def build_vehicle(item):
    vehicle = schemas.VehicleBase
    vehicle.veiculo = item.veiculo
    vehicle.ano = item.ano
    vehicle.descricao = item.descricao
    vehicle.vendido = item.vendido
    vehicle.created = item.created
    vehicle.updated = item.updated
    vehicle.marca = item.marca.marca
    return vehicle


def build_json_output(result):
    item_data = jsonable_encoder(result)
    item_model = schemas.VehicleElastic(**item_data)
    model: dict = jsonable_encoder(item_model.copy())
    model.update({"marca": model["marca"]["marca"]})
    return model


def es_indexing(result):
    model = build_json_output(result)
    es.post(model)


def es_search_id(vehicle_id, key):
    body = {
        "query": {
            "match": {
                "id": f"{vehicle_id}"
            }
        }
    }
    response = es.search(body)
    if response["hits"]["hits"]:
        return response["hits"]["hits"][0][f"{key}"]


def es_update_doc(doc_id, result):
    model = build_json_output(result)
    es.update(doc_id, model)


def get_terms(q: str):
    result = list()
    query = {
        "query": {
            "multi_match": {
                "query": q,
                "fields": ["veiculo", "marca", "descricao"]
            }
        }
    }
    response = es.search(query)
    response = response["hits"]["hits"]
    for item in response:
        model = schemas.VehicleBase(**item["_source"])
        result.append(model)
    return result


def unsold(db):
    return {"result": f"Existe {len(crud.unsold(db))} veiculo(s) não vendido(s)"}


def distribution(db):
    results = []
    response = crud.distribution(db)
    for item in response:
        results.append({item._data[0].marca:  f"{item._data[1]} veiculos"})
    return results


def last_register(db):
    results = []
    response = crud.last_register(db)
    for item in response:
        response = jsonable_encoder(item)
        model = schemas.Vehicle(**response)
        model.marca = item.marca.marca
        results.append(model)
    return results
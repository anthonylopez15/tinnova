from fastapi.encoders import jsonable_encoder

from app import schemas
from app import crud


def create_vehicle(db, vehicle):
    result = crud.create(db, vehicle)
    if result:
        vehicle.marca = result.marca.marca
    return vehicle


def find_by_id(db, id):
    return crud.get_id(db, id)


def update_vehicle(vehicle_id, vehicle, db):
    result = crud.update(db, vehicle, vehicle_id)
    if result:
        vehicle.marca = result.marca.marca
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


def delete(vehicle_id, db):
    return f"{crud.remove(vehicle_id)} row deleted"


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

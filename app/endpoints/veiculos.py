from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import schemas
from app.db import controller
from app.db.crud import list_make
from app.db.deps import get_db

router = APIRouter()


@router.get("/marcas", response_model=List[schemas.Make], summary="Lista das marcas")
def get_make(db: Session = Depends(get_db)):
    return list_make(db)

@router.post("/marcas")
def create_make(make: schemas.Make, db: Session = Depends(get_db)):
    return controller.create_make(make, db)


@router.get("/veiculos", response_model=List[schemas.VehicleBase], summary="Lista todos os veiculos")
def find_all(db: Session = Depends(get_db)):
    return controller.get_all(db)


@router.get("/veiculos/unsold", summary="Lista de veiculos não vendidos")
def unsold(db: Session = Depends(get_db)):
    return controller.unsold(db)


@router.get("/veiculos/distribution-by-maker", summary="Distibuição de veiculos por fabricante")
def distribution(db: Session = Depends(get_db)):
    return controller.distribution(db)



@router.get("/veiculos/last-register", summary="Registro de carros da ultima semana")
def last_register(db: Session = Depends(get_db)):
    return controller.last_register(db)

@router.get("/veiculos/find", summary="Pesquisa por termo ou conjunto de termos")
def find(q: str):
    return controller.get_terms(q)


@router.get("/veiculos/{id}", summary="Buscar veiculo por ID")
def find_by_id(id: int, db: Session = Depends(get_db)):
    return controller.find_by_id(db, id)


@router.post("/veiculos", response_model=schemas.VehicleBase, summary="Criar novos veiculos")
def create(vehicle: schemas.VehicleBase, db: Session = Depends(get_db)):
    return controller.create_vehicle(db, vehicle)


@router.put("/veiculos/{id}", response_model=schemas.VehicleBase, summary="Atualizar dados veiculo")
def update(id: int,
           vehicle: schemas.VehicleBase,
           db: Session = Depends(get_db)):
    return controller.update_vehicle(id, vehicle, db)


@router.patch("/veiculos/{id}", summary="Atualizar parte veiculo")
def update(id: int,
           vehicle: schemas.VehicleBase,
           db: Session = Depends(get_db)):
    return controller.patch_vehicle(id, vehicle, db)


@router.delete("/veiculos/{id}", summary="Deletar um veiculo")
def delete(id: int):
    return controller.delete(id)

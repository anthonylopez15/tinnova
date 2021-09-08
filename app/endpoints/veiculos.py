from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import schemas
from app.db import controller
from app.db.crud import list_make
from app.db.deps import get_db

router = APIRouter()


@router.get("/marcas", response_model=List[schemas.Make])
def get_make(db: Session = Depends(get_db)):
    return list_make(db)


@router.get("/veiculos", response_model=List[schemas.VehicleBase])
def find_all(db: Session = Depends(get_db)):
    return controller.get_all(db)


@router.get("/veiculos/find")
def find(q: str):
    return controller.get_terms(q)


@router.get("/veiculos/{id}")
def find_by_id(id: int, db: Session = Depends(get_db)):
    return controller.find_by_id(db, id)


@router.post("/veiculos", response_model=schemas.VehicleBase)
def create(vehicle: schemas.VehicleBase, db: Session = Depends(get_db)):
    return controller.create_vehicle(db, vehicle)


@router.put("/veiculos/{id}", response_model=schemas.VehicleBase)
def update(id: int,
           vehicle: schemas.VehicleBase,
           db: Session = Depends(get_db)):
    return controller.update_vehicle(id, vehicle, db)


@router.patch("/veiculos/{id}")
def update(id: int,
           vehicle: schemas.VehicleBase,
           db: Session = Depends(get_db)):
    return controller.patch_vehicle(id, vehicle, db)


@router.delete("/veiculos/{id}")
def delete(id: int):
    return controller.delete(id)

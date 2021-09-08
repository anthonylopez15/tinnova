from sqlalchemy import delete
from fastapi import HTTPException

from sqlalchemy.orm import Session
from app import models, schemas
from app.database import engine


def find_all(db: Session):
    return db.query(models.Vehicle).all()


# TODO incompleto
def find(db: Session, q: str):
    return db.query(models.Vehicle).filter(models.Vehicle)


def get_id(db: Session, id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.id == id).first()


def create(db: Session, vehicle):
    db_item = models.Vehicle(**vehicle.dict())
    db_marca = db.query(models.Make).filter(models.Make.marca.ilike(db_item.marca)).first()
    if not db_marca:
        raise HTTPException(status_code=404, detail="Brand not Found")
    db_item.marca = db_marca
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def list_make(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Make).offset(skip).limit(limit).all()


def update(db: Session, vehicle, vehicle_id):
    db_item = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).one_or_none()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Vehicle not Found")

    db_marca = db.query(models.Make).filter(models.Make.marca.ilike(vehicle.marca)).first()
    del vehicle.marca, vehicle.marca_id
    if not db_marca:
        raise HTTPException(status_code=404, detail="Brand not Found")

    for var, value in vars(vehicle).items():
        setattr(db_item, var, value) if value else None

    db_item.marca = db_marca
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def remove(vehicle_id):
    conn = engine.connect()
    stmt = delete(models.Vehicle).where((models.Vehicle.id == vehicle_id))
    result = conn.execute(stmt)
    return result.rowcount

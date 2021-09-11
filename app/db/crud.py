from datetime import datetime, timedelta

from fastapi import HTTPException
from sqlalchemy import delete, func
from sqlalchemy.orm import Session

from app.db import models
from app.db.database import engine


def find_all(db: Session):
    return db.query(models.Vehicle).all()


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


def list_make(db: Session):
    return db.query(models.Make).all()


def update(db: Session, vehicle, vehicle_id):
    db_item = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).one_or_none()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Vehicle not Found")

    db_marca = db.query(models.Make).filter(models.Make.marca.ilike(vehicle.marca)).first()
    del vehicle.marca
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


def unsold(db: Session):
    return db.query(models.Vehicle).filter(models.Vehicle.vendido == False).all()


def distribution(db: Session):
    curs = db.query(models.Make,
                    func.count(models.Vehicle.marca_id)) \
        .join(models.Vehicle.marca) \
        .group_by(models.Make.id) \
        .all()
    return curs


def last_register(db: Session):
    curs = db.query(models.Vehicle)\
        .filter(models.Vehicle.created <= datetime.now())\
        .filter(models.Vehicle.created >= datetime.now() - timedelta(days=7)).all()
    return curs


def create_make(db: Session, make):
    db_item = models.Make(**make.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
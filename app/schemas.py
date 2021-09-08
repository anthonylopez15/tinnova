from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class Make(BaseModel):
    marca: Optional[str]

    class Config:
        orm_mode = True


class VehicleBase(BaseModel):
    veiculo: Optional[str]
    ano: Optional[int] = Field(None, example="1990")
    marca: Optional[str]
    descricao: Optional[str]
    vendido: Optional[bool]
    created: Optional[datetime]
    updated: Optional[datetime]

    class Config:
        orm_mode = True


class Vehicle(VehicleBase):
    marca: Make

class VehicleUpdate(VehicleBase):
    marca: Optional[Make]
    marca_id: Optional[int]

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Make(BaseModel):
    marca: Optional[str]

    class Config:
        orm_mode = True


class VehicleBase(BaseModel):
    veiculo: Optional[str] = Field(None, example="Onix")
    ano: Optional[int] = Field(None, example="2020")
    marca: Optional[str] = Field(None, example="CHEVROLET")
    descricao: Optional[str] = Field(None, example="Opcional")
    vendido: Optional[bool] = Field(None, example="false")
    created: Optional[datetime]
    updated: Optional[datetime]

    class Config:
        orm_mode = True


class Vehicle(VehicleBase):
    marca: Optional[Make]

class VehicleUpdate(VehicleBase):
    marca: Optional[Make]
    marca_id: Optional[int]

class VehicleElastic(VehicleUpdate):
    id: Optional[int]
    marca: Optional[Make]

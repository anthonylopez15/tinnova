from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Vehicle(Base):
    __tablename__ = "veiculo"

    id = Column(Integer, primary_key=True, index=True)
    veiculo = Column(String)
    marca_id = Column(Integer, ForeignKey("marca.id"))
    marca = relationship("Make")
    ano = Column(Integer)
    descricao = Column(String)
    vendido = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now())
    updated = Column(DateTime)

class Make(Base):
    __tablename__ = "marca"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=True)
    value = Column(String)
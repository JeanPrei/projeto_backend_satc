from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class VeiculoCreate(BaseModel):
    placa: str
    modelo: str
    capacidade_kg: Decimal
    disponivel: bool = True


class VeiculoUpdate(BaseModel):
    placa: str | None = None
    modelo: str | None = None
    capacidade_kg: Decimal | None = None
    disponivel: bool | None = None


class VeiculoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    placa: str
    modelo: str
    capacidade_kg: Decimal
    disponivel: bool
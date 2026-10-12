from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class RotaCreate(BaseModel):
    origem: str
    destino: str
    distancia_km: Decimal
    tempo_estimado_horas: Decimal | None = None


class RotaUpdate(BaseModel):
    origem: str | None = None
    destino: str | None = None
    distancia_km: Decimal | None = None
    tempo_estimado_horas: Decimal | None = None


class RotaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    origem: str
    destino: str
    distancia_km: Decimal
    tempo_estimado_horas: Decimal | None
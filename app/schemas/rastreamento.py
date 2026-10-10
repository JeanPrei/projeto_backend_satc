from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RastreamentoCreate(BaseModel):
    entrega_id: int
    localizacao: str
    data_hora: datetime
    observacao: str | None = None


class RastreamentoUpdate(BaseModel):
    entrega_id: int | None = None
    localizacao: str | None = None
    data_hora: datetime | None = None
    observacao: str | None = None


class RastreamentoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    entrega_id: int
    localizacao: str
    data_hora: datetime
    observacao: str | None
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EntregaCreate(BaseModel):
    rota_id: int
    veiculo_id: int
    destinatario: str
    previsao_entrega: datetime | None = None
    status: str


class EntregaUpdate(BaseModel):
    rota_id: int | None = None
    veiculo_id: int | None = None
    destinatario: str | None = None
    previsao_entrega: datetime | None = None
    status: str | None = None


class EntregaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    rota_id: int
    veiculo_id: int
    destinatario: str
    previsao_entrega: datetime | None
    status: str
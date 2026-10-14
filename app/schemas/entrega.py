from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class EntregaCreate(BaseModel):
    rota_id: int = Field(gt=0)
    veiculo_id: int = Field(gt=0)
    destinatario: str = Field(min_length=1, max_length=100)
    previsao_entrega: datetime | None = None
    status: str = Field(min_length=1, max_length=100)

    @field_validator("destinatario", "status")
    @classmethod
    def remover_espacos(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError("O campo não pode ficar vazio.")

        return valor


class EntregaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    rota_id: int
    veiculo_id: int
    destinatario: str
    previsao_entrega: datetime | None
    status: str
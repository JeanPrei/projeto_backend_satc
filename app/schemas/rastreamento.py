from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class RastreamentoCreate(BaseModel):
    entrega_id: int = Field(gt=0)
    localizacao: str = Field(min_length=1, max_length=200)
    data_hora: datetime
    observacao: str | None = None

    @field_validator("localizacao")
    @classmethod
    def validar_localizacao(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError("A localização não pode ficar vazia.")

        return valor

    @field_validator("observacao")
    @classmethod
    def validar_observacao(cls, valor: str | None) -> str | None:
        if valor is not None:
            valor = valor.strip()

            if not valor:
                return None

        return valor


class RastreamentoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    entrega_id: int
    localizacao: str
    data_hora: datetime
    observacao: str | None
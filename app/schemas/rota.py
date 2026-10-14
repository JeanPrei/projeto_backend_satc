from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class RotaCreate(BaseModel):
    origem: str = Field(min_length=1, max_length=100)
    destino: str = Field(min_length=1, max_length=100)
    distancia_km: Decimal = Field(
        gt=0,
        max_digits=10,
        decimal_places=2,
    )
    tempo_estimado_horas: Decimal | None = Field(
        default=None,
        gt=0,
        max_digits=10,
        decimal_places=2,
    )

    @field_validator("origem", "destino")
    @classmethod
    def validar_local(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError("O campo não pode ficar vazio.")

        return valor


class RotaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    origem: str
    destino: str
    distancia_km: Decimal
    tempo_estimado_horas: Decimal | None
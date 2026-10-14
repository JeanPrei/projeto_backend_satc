from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class VeiculoCreate(BaseModel):
    placa: str = Field(min_length=1, max_length=10)
    modelo: str = Field(min_length=1, max_length=100)
    capacidade_kg: Decimal = Field(
        gt=0,
        max_digits=10,
        decimal_places=2,
    )
    disponivel: bool = True

    @field_validator("placa", "modelo")
    @classmethod
    def remover_espacos(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError("O campo não pode ficar vazio.")

        return valor

    @field_validator("placa")
    @classmethod
    def normalizar_placa(cls, valor: str) -> str:
        return valor.upper()


class VeiculoUpdate(BaseModel):
    placa: str | None = Field(default=None, min_length=1, max_length=10)
    modelo: str | None = Field(default=None, min_length=1, max_length=100)
    capacidade_kg: Decimal | None = Field(
        default=None,
        gt=0,
        max_digits=10,
        decimal_places=2,
    )
    disponivel: bool | None = None

    @field_validator("placa", "modelo")
    @classmethod
    def remover_espacos(cls, valor: str | None) -> str | None:
        if valor is None:
            return valor

        valor = valor.strip()

        if not valor:
            raise ValueError("O campo não pode ficar vazio.")

        return valor

    @field_validator("placa")
    @classmethod
    def normalizar_placa(cls, valor: str | None) -> str | None:
        if valor is None:
            return valor

        return valor.upper()


class VeiculoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    placa: str
    modelo: str
    capacidade_kg: Decimal
    disponivel: bool

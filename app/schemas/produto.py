from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ProdutoCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    codigo: str | None = Field(default=None, max_length=30)
    descricao: str | None = None
    preco: Decimal = Field(gt=0, max_digits=10, decimal_places=2)

    @field_validator("nome", "codigo")
    @classmethod
    def remover_espacos(cls, valor: str | None) -> str | None:
        if valor is None:
            return valor

        valor = valor.strip()

        if not valor:
            raise ValueError("O campo não pode ficar vazio.")

        return valor


class ProdutoUpdate(BaseModel):
    nome: str | None = Field(default=None, min_length=1, max_length=100)
    codigo: str | None = Field(default=None, max_length=30)
    descricao: str | None = None
    preco: Decimal | None = Field(
        default=None, gt=0, max_digits=10, decimal_places=2
    )

    @field_validator("nome", "codigo")
    @classmethod
    def remover_espacos(cls, valor: str | None) -> str | None:
        if valor is None:
            return valor

        valor = valor.strip()

        if not valor:
            raise ValueError("O campo não pode ficar vazio.")

        return valor


class ProdutoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    codigo: str | None
    descricao: str | None
    preco: Decimal

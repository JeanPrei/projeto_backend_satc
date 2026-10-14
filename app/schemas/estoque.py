from pydantic import BaseModel, ConfigDict, Field, field_validator


class EstoqueCreate(BaseModel):
    produto_id: int = Field(gt=0)
    localizacao: str = Field(min_length=1, max_length=100)
    quantidade: int = Field(default=0, ge=0)
    estoque_minimo: int = Field(default=0, ge=0)

    @field_validator("localizacao")
    @classmethod
    def validar_localizacao(cls, valor: str) -> str:
        valor = valor.strip()

        if not valor:
            raise ValueError("A localização não pode ficar vazia.")

        return valor


class EstoqueUpdate(BaseModel):
    produto_id: int | None = Field(default=None, gt=0)
    localizacao: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
    quantidade: int | None = Field(default=None, ge=0)
    estoque_minimo: int | None = Field(default=None, ge=0)

    @field_validator("localizacao")
    @classmethod
    def validar_localizacao(cls, valor: str | None) -> str | None:
        if valor is None:
            return valor

        valor = valor.strip()

        if not valor:
            raise ValueError("A localização não pode ficar vazia.")

        return valor


class EstoqueRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    produto_id: int
    localizacao: str
    quantidade: int
    estoque_minimo: int
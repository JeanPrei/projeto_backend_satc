from pydantic import BaseModel, ConfigDict


class EstoqueCreate(BaseModel):
    produto_id: int
    localizacao: str
    quantidade: int = 0
    estoque_minimo: int = 0


class EstoqueUpdate(BaseModel):
    produto_id: int | None = None
    localizacao: str | None = None
    quantidade: int | None = None
    estoque_minimo: int | None = None


class EstoqueRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    produto_id: int
    localizacao: str
    quantidade: int
    estoque_minimo: int
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProdutoCreate(BaseModel):
	nome: str
	codigo: str | None = None
	descricao: str | None = None
	preco: Decimal


class ProdutoUpdate(BaseModel):
	nome: str | None = None
	codigo: str | None = None
	descricao: str | None = None
	preco: Decimal | None = None


class ProdutoRead(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int
	nome: str
	codigo: str | None
	descricao: str | None
	preco: Decimal

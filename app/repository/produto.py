
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.produto import Produto


class ProdutoRepository:
    """Responsável pelo acesso aos dados de produtos."""

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: Produto) -> Produto:
        self.db.add(produto)
        self.db.commit()
        self.db.refresh(produto)
        return produto

    def listar(self) -> list[Produto]:
        consulta = select(Produto).order_by(Produto.id)
        return list(self.db.scalars(consulta).all())

    def buscar_por_id(self, produto_id: int) -> Produto | None:
        return self.db.get(Produto, produto_id)

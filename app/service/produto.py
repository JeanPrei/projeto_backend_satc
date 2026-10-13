
from sqlalchemy.orm import Session

from app.models.produto import Produto
from app.repository.produto import ProdutoRepository


class ProdutoService:
    """Contém as regras de negócio relacionadas a produtos."""

    def __init__(self, db: Session):
        self.repository = ProdutoRepository(db)

    def criar(self, dados: dict) -> Produto:
        produto = Produto(**dados)
        return self.repository.criar(produto)

    def listar(self) -> list[Produto]:
        return self.repository.listar()

    def buscar_por_id(self, produto_id: int) -> Produto:
        produto = self.repository.buscar_por_id(produto_id)

        if produto is None:
            raise ValueError(
                f"Produto com ID {produto_id} não encontrado."
            )

        return produto

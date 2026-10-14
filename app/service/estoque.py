from sqlalchemy.orm import Session

from app.models.estoque import Estoque
from app.repository.estoque import EstoqueRepository
from app.repository.produto import ProdutoRepository


class EstoqueService:
    """Contém as regras de negócio relacionadas ao estoque."""

    def __init__(self, db: Session):
        self.repository = EstoqueRepository(db)
        self.produto_repository = ProdutoRepository(db)

    def criar(self, dados: dict) -> Estoque:
        produto = self.produto_repository.buscar_por_id(
            dados["produto_id"]
        )

        if produto is None:
            raise ValueError(
                f"Produto com ID {dados['produto_id']} não encontrado."
            )

        estoque = Estoque(**dados)
        return self.repository.criar(estoque)

    def listar(self) -> list[Estoque]:
        return self.repository.listar()

    def buscar_por_id(self, estoque_id: int) -> Estoque:
        estoque = self.repository.buscar_por_id(estoque_id)

        if estoque is None:
            raise ValueError(
                f"Estoque com ID {estoque_id} não encontrado."
            )

        return estoque


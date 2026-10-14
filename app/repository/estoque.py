from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.estoque import Estoque


class EstoqueRepository:
    """Responsável pelo acesso aos dados de estoque."""

    def __init__(self, db: Session):
        self.db = db

    def criar(self, estoque: Estoque) -> Estoque:
        self.db.add(estoque)
        self.db.commit()
        self.db.refresh(estoque)
        return estoque

    def listar(self) -> list[Estoque]:
        consulta = select(Estoque).order_by(Estoque.id)
        return list(self.db.scalars(consulta).all())

    def buscar_por_id(self, estoque_id: int) -> Estoque | None:
        return self.db.get(Estoque, estoque_id)


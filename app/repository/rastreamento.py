from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.rastreamento import Rastreamento


class RastreamentoRepository:
    """Responsável pelo acesso aos dados de rastreamento."""

    def __init__(self, db: Session):
        self.db = db

    def criar(self, rastreamento: Rastreamento) -> Rastreamento:
        self.db.add(rastreamento)
        self.db.commit()
        self.db.refresh(rastreamento)
        return rastreamento

    def listar(self) -> list[Rastreamento]:
        consulta = select(Rastreamento).order_by(Rastreamento.id)
        return list(self.db.scalars(consulta).all())

    def buscar_por_id(
        self, rastreamento_id: int
    ) -> Rastreamento | None:
        return self.db.get(Rastreamento, rastreamento_id)
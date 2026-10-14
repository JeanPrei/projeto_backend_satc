from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.entrega import Entrega


class EntregaRepository:
    """Responsável pelo acesso aos dados de entregas."""

    def __init__(self, db: Session):
        self.db = db

    def criar(self, entrega: Entrega) -> Entrega:
        self.db.add(entrega)
        self.db.commit()
        self.db.refresh(entrega)
        return entrega

    def listar(self) -> list[Entrega]:
        consulta = select(Entrega).order_by(Entrega.id)
        return list(self.db.scalars(consulta).all())

    def buscar_por_id(self, entrega_id: int) -> Entrega | None:
        return self.db.get(Entrega, entrega_id)
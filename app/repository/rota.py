from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.rota import Rota


class RotaRepository:
    """Responsável pelo acesso aos dados de rotas."""

    def __init__(self, db: Session):
        self.db = db

    def criar(self, rota: Rota) -> Rota:
        self.db.add(rota)
        self.db.commit()
        self.db.refresh(rota)
        return rota

    def listar(self) -> list[Rota]:
        consulta = select(Rota).order_by(Rota.id)
        return list(self.db.scalars(consulta).all())

    def buscar_por_id(self, rota_id: int) -> Rota | None:
        return self.db.get(Rota, rota_id)
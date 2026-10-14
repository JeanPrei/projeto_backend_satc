from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.veiculo import Veiculo


class VeiculoRepository:
    """Responsável pelo acesso aos dados de veículos."""

    def __init__(self, db: Session):
        self.db = db

    def criar(self, veiculo: Veiculo) -> Veiculo:
        self.db.add(veiculo)
        self.db.commit()
        self.db.refresh(veiculo)
        return veiculo

    def listar(self) -> list[Veiculo]:
        consulta = select(Veiculo).order_by(Veiculo.id)
        return list(self.db.scalars(consulta).all())

    def buscar_por_id(self, veiculo_id: int) -> Veiculo | None:
        return self.db.get(Veiculo, veiculo_id)
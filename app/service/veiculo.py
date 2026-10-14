from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.veiculo import Veiculo
from app.repository.veiculo import VeiculoRepository


class VeiculoService:
    """Responsável pelas regras de negócio dos veículos."""

    def __init__(self, db: Session):
        self.repository = VeiculoRepository(db)
        self.db = db

    def criar(self, dados: dict) -> Veiculo:
        veiculo = Veiculo(**dados)

        try:
            return self.repository.criar(veiculo)
        except IntegrityError as erro:
            self.db.rollback()
            raise ValueError(
                "Não foi possível cadastrar o veículo. "
                "Verifique se a placa já está cadastrada."
            ) from erro

    def listar(self) -> list[Veiculo]:
        return self.repository.listar()

    def buscar_por_id(self, veiculo_id: int) -> Veiculo | None:
        return self.repository.buscar_por_id(veiculo_id)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.rota import Rota
from app.repository.rota import RotaRepository


class RotaService:
    """Responsável pelas regras de negócio das rotas."""

    def __init__(self, db: Session):
        self.repository = RotaRepository(db)
        self.db = db

    def criar(self, dados: dict) -> Rota:
        rota = Rota(**dados)

        try:
            return self.repository.criar(rota)
        except IntegrityError as erro:
            self.db.rollback()
            raise ValueError(
                "Não foi possível cadastrar a rota. "
                "Verifique os dados informados."
            ) from erro

    def listar(self) -> list[Rota]:
        return self.repository.listar()

    def buscar_por_id(self, rota_id: int) -> Rota | None:
        return self.repository.buscar_por_id(rota_id)
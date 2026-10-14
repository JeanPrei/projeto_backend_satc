from sqlalchemy.orm import Session

from app.models.entrega import Entrega
from app.models.rota import Rota
from app.models.veiculo import Veiculo
from app.repository.entrega import EntregaRepository


class EntregaService:
    """Responsável pelas regras de negócio das entregas."""

    def __init__(self, db: Session):
        self.db = db
        self.repository = EntregaRepository(db)

    def criar(self, dados: dict) -> Entrega:
        rota = self.db.get(Rota, dados["rota_id"])

        if rota is None:
            raise ValueError("A rota informada não existe.")

        veiculo = self.db.get(Veiculo, dados["veiculo_id"])

        if veiculo is None:
            raise ValueError("O veículo informado não existe.")

        entrega = Entrega(**dados)
        return self.repository.criar(entrega)

    def listar(self) -> list[Entrega]:
        return self.repository.listar()

    def buscar_por_id(self, entrega_id: int) -> Entrega | None:
        return self.repository.buscar_por_id(entrega_id)
from sqlalchemy.orm import Session

from app.models.entrega import Entrega
from app.models.rastreamento import Rastreamento
from app.repository.rastreamento import RastreamentoRepository


class RastreamentoService:
    """Responsável pelas regras de negócio dos rastreamentos."""

    def __init__(self, db: Session):
        self.db = db
        self.repository = RastreamentoRepository(db)

    def criar(self, dados: dict) -> Rastreamento:
        entrega = self.db.get(Entrega, dados["entrega_id"])

        if entrega is None:
            raise ValueError("A entrega informada não existe.")

        rastreamento = Rastreamento(**dados)
        return self.repository.criar(rastreamento)

    def listar(self) -> list[Rastreamento]:
        return self.repository.listar()

    def buscar_por_id(
        self, rastreamento_id: int
    ) -> Rastreamento | None:
        return self.repository.buscar_por_id(rastreamento_id)
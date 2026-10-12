from decimal import Decimal

from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Rota(Base):
    __tablename__ = "rotas"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    origem: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    destino: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    distancia_km: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    tempo_estimado_horas: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True,
    )

    entregas: Mapped[list["Entrega"]] = relationship(
        back_populates="rota",
    )
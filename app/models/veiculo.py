from decimal import Decimal

from sqlalchemy import Boolean, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Veiculo(Base):
    __tablename__ = "veiculos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    placa: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        unique=True,
    )

    modelo: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    capacidade_kg: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    disponivel: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    entregas: Mapped[list["Entrega"]] = relationship(
        back_populates="veiculo",
    )
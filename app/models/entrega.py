from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Entrega(Base):
    __tablename__ = "entregas"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    rota_id: Mapped[int] = mapped_column(
        ForeignKey("rotas.id"),
        nullable=False,
    )

    veiculo_id: Mapped[int] = mapped_column(
        ForeignKey("veiculos.id"),
        nullable=False,
    )

    destinatario: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    previsao_entrega: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    rota: Mapped["Rota"] = relationship(
        back_populates="entregas",
    )

    veiculo: Mapped["Veiculo"] = relationship(
        back_populates="entregas",
    )

    rastreamentos: Mapped[list["Rastreamento"]] = relationship(
        back_populates="entrega",
    )
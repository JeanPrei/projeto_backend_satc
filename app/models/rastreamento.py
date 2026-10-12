from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Rastreamento(Base):
    __tablename__ = "rastreamentos"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    entrega_id: Mapped[int] = mapped_column(
        ForeignKey("entregas.id"),
        nullable=False,
    )

    localizacao: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    data_hora: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    observacao: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    entrega: Mapped["Entrega"] = relationship(
        back_populates="rastreamentos",
    )
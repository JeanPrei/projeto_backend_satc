from decimal import Decimal

from sqlalchemy import Numeric, String, Text, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.db.base import Base


class Produto(Base):
    __tablename__ = "produtos"    

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    codigo: Mapped[str] = mapped_column(
        String(30),
        nullable=True,
        unique=True,
    )

    descricao: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    preco: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    estoques: Mapped[list["Estoque"]] = relationship(
        back_populates="produto",
        cascade="all",
    )
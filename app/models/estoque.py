from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Estoque(Base):
	__tablename__ = "estoques"

	id: Mapped[int] = mapped_column(
		primary_key=True,
		autoincrement=True,
	)

	produto_id: Mapped[int] = mapped_column(
		ForeignKey("produtos.id"),
		nullable=False,
	)

	localizacao: Mapped[str] = mapped_column(
		String(100),
		nullable=False,
	)

	quantidade: Mapped[int] = mapped_column(
		Integer,
		nullable=False,
		default=0,
	)

	estoque_minimo: Mapped[int] = mapped_column(
		Integer,
		nullable=False,
		default=0,
	)

	produto: Mapped["Produto"] = relationship(
		back_populates="estoques",
	)

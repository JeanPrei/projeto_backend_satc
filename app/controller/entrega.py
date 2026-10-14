from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.entrega import EntregaCreate, EntregaRead
from app.service.entrega import EntregaService


router = APIRouter(
    prefix="/entregas",
    tags=["Entregas"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/",
    response_model=EntregaRead,
    status_code=status.HTTP_201_CREATED
)
def criar_entrega(
    dados: EntregaCreate,
    db: Session = Depends(get_db)
):
    service = EntregaService(db)

    try:
        return service.criar(dados.model_dump())
    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        ) from erro


@router.get("/", response_model=list[EntregaRead])
def listar_entregas(db: Session = Depends(get_db)):
    service = EntregaService(db)
    return service.listar()


@router.get("/{entrega_id}", response_model=EntregaRead)
def buscar_entrega(
    entrega_id: int,
    db: Session = Depends(get_db)
):
    service = EntregaService(db)
    entrega = service.buscar_por_id(entrega_id)

    if entrega is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Entrega não encontrada."
        )

    return entrega
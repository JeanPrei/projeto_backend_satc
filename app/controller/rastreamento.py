from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.rastreamento import RastreamentoCreate, RastreamentoRead
from app.service.rastreamento import RastreamentoService


router = APIRouter(
    prefix="/rastreamentos",
    tags=["Rastreamentos"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/",
    response_model=RastreamentoRead,
    status_code=status.HTTP_201_CREATED
)
def criar_rastreamento(
    dados: RastreamentoCreate,
    db: Session = Depends(get_db)
):
    service = RastreamentoService(db)

    try:
        return service.criar(dados.model_dump())
    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        ) from erro


@router.get("/", response_model=list[RastreamentoRead])
def listar_rastreamentos(db: Session = Depends(get_db)):
    service = RastreamentoService(db)
    return service.listar()


@router.get("/{rastreamento_id}", response_model=RastreamentoRead)
def buscar_rastreamento(
    rastreamento_id: int,
    db: Session = Depends(get_db)
):
    service = RastreamentoService(db)
    rastreamento = service.buscar_por_id(rastreamento_id)

    if rastreamento is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rastreamento não encontrado."
        )

    return rastreamento
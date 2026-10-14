from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.rota import RotaCreate, RotaRead
from app.service.rota import RotaService


router = APIRouter(prefix="/rotas", tags=["Rotas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/",
    response_model=RotaRead,
    status_code=status.HTTP_201_CREATED,
)
def criar_rota(
    dados: RotaCreate,
    db: Session = Depends(get_db),
):
    service = RotaService(db)

    try:
        return service.criar(dados.model_dump())
    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro),
        ) from erro


@router.get("/", response_model=list[RotaRead])
def listar_rotas(db: Session = Depends(get_db)):
    return RotaService(db).listar()


@router.get("/{rota_id}", response_model=RotaRead)
def buscar_rota(
    rota_id: int,
    db: Session = Depends(get_db),
):
    rota = RotaService(db).buscar_por_id(rota_id)

    if rota is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rota não encontrada.",
        )

    return rota
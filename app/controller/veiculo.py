from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.veiculo import (
    VeiculoCreate,
    VeiculoRead,
    VeiculoUpdate,
)
from app.service.veiculo import VeiculoService


router = APIRouter(prefix="/veiculos", tags=["Veículos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/",
    response_model=VeiculoRead,
    status_code=status.HTTP_201_CREATED,
)
def criar_veiculo(
    dados: VeiculoCreate,
    db: Session = Depends(get_db),
):
    service = VeiculoService(db)

    try:
        return service.criar(dados.model_dump())
    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro),
        ) from erro


@router.get("/", response_model=list[VeiculoRead])
def listar_veiculos(db: Session = Depends(get_db)):
    return VeiculoService(db).listar()


@router.get("/{veiculo_id}", response_model=VeiculoRead)
def buscar_veiculo(
    veiculo_id: int,
    db: Session = Depends(get_db),
):
    veiculo = VeiculoService(db).buscar_por_id(veiculo_id)

    if veiculo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Veículo não encontrado.",
        )

    return veiculo
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.controller.produto import obter_db
from app.schemas.estoque import EstoqueCreate, EstoqueRead
from app.service.estoque import EstoqueService


router = APIRouter(prefix="/estoques", tags=["Estoques"])


@router.post("/", response_model=EstoqueRead, status_code=201)
def criar_estoque(
    dados: EstoqueCreate,
    db: Session = Depends(obter_db),
):
    try:
        return EstoqueService(db).criar(
            dados.model_dump()
        )
    except ValueError as erro:
        raise HTTPException(
            status_code=404,
            detail=str(erro),
        ) from erro
    except IntegrityError as erro:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Não foi possível cadastrar o estoque. Verifique os dados informados.",
        ) from erro


@router.get("/", response_model=list[EstoqueRead])
def listar_estoques(
    db: Session = Depends(obter_db),
):
    return EstoqueService(db).listar()


@router.get("/{estoque_id}", response_model=EstoqueRead)
def buscar_estoque(
    estoque_id: int,
    db: Session = Depends(obter_db),
):
    try:
        return EstoqueService(db).buscar_por_id(estoque_id)
    except ValueError as erro:
        raise HTTPException(
            status_code=404,
            detail=str(erro),
        ) from erro

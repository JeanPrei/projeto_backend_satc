from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.produto import ProdutoCreate, ProdutoRead
from app.service.produto import ProdutoService


router = APIRouter(prefix="/produtos", tags=["Produtos"])


def obter_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProdutoRead, status_code=201)
def criar_produto(
    dados: ProdutoCreate,
    db: Session = Depends(obter_db),
):
    try:
        return ProdutoService(db).criar(
            dados.model_dump()
        )
    except IntegrityError as erro:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Não foi possível cadastrar o produto. Verifique se o código já existe.",
        ) from erro


@router.get("/", response_model=list[ProdutoRead])
def listar_produtos(
    db: Session = Depends(obter_db),
):
    return ProdutoService(db).listar()


@router.get("/{produto_id}", response_model=ProdutoRead)
def buscar_produto(
    produto_id: int,
    db: Session = Depends(obter_db),
):
    try:
        return ProdutoService(db).buscar_por_id(produto_id)
    except ValueError as erro:
        raise HTTPException(
            status_code=404,
            detail=str(erro),
        ) from erro
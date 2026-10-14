from fastapi import FastAPI

from app.controller.produto import router as produto_router
from app.controller.estoque import router as estoque_router
from app.controller.veiculo import router as veiculo_router
from app.controller.rota import router as rota_router
from app.controller.entrega import router as entrega_router
from app.controller.rastreamento import router as rastreamento_router


app = FastAPI(
    title="Logística e Cadeia de Suprimentos - Projeto Backend SATC",
    version="1.0.0",
)

app.include_router(produto_router)
app.include_router(estoque_router)
app.include_router(veiculo_router)
app.include_router(rota_router)
app.include_router(entrega_router)
app.include_router(rastreamento_router)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
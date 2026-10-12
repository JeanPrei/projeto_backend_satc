from fastapi import FastAPI


app = FastAPI(title="Logística e Cadeia de Suprimentos - Projeto Backend SATC", version="1.0.0")


@app.get("/health")
def health_check() -> dict[str, str]:
	return {"status": "ok"}
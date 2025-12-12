from fastapi import FastAPI
from pydantic_settings import BaseSettings

# 1. Configuração rápida (num cenário real, isso iria para core/config.py)
class Settings(BaseSettings):
    DATABASE_URL: str
    RABBITMQ_URL: str

settings = Settings()

# 2. Inicialização do App
app = FastAPI(
    title="Simonia Core Service",
    version="0.1.0",
    root_path="/api/v1/core", 
    docs_url="/docs",
    openapi_url="/openapi.json"
)

@app.get("/")
async def root():
    return {
        "message": "Bem-vindo ao Simonia Core Service",
        "status": "online",
        "db_connection": settings.DATABASE_URL.split("@")[1] 
    }

@app.get("/health")
async def health_check():
    return {"status": "ok"}
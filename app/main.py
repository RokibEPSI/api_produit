from fastapi import FastAPI
from app.routes import router
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Produits - Paye ton Kawa")
app.include_router(router, prefix="/produits", tags=["Produits"])

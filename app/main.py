from fastapi import FastAPI
from . import models, database, routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="API Produits – Paye Ton Kawa")

app.include_router(routes.router, prefix="/products", tags=["Produits"])

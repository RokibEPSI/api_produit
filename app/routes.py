from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal
from app.auth import get_current_user
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import verify_password, create_access_token
from app.models import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ProductOut)
def create(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/", response_model=list[schemas.ProductOut])
def list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@router.get("/{product_id}", response_model=schemas.ProductOut)
def read(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return product

@router.put("/{product_id}", response_model=schemas.ProductOut)
def update(product_id: int, data: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, data)

@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, product_id)

@router.post("/produits/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Identifiants invalides")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/produits-proteges/", dependencies=[Depends(get_current_user)])
def read_secure_data():
    return {"msg": "Accès autorisé"}

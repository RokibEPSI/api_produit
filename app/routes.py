from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from fastapi.encoders import jsonable_encoder
from .database import SessionLocal
from app.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import verify_password, create_access_token
from app.models import User
from app.event_bus import publish_event
from app.auth import get_password_hash
from app.schemas import UserCreate, Token, UserOut



router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ProductOut, dependencies=[Depends(get_current_user)])
def create(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = crud.create_product(db, product)
    publish_event("products.created", jsonable_encoder(new_product))
    return new_product

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
    updated_product = crud.update_product(db, product_id, data)
    publish_event("products.updated", jsonable_encoder(updated_product))
    return updated_product


@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    crud.delete_product(db, product_id)
    publish_event("products.deleted", {"id": product_id})
    return {"message": "Produit supprimé avec succès"}


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

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_exists = db.query(User).filter(User.username == user.username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Nom d'utilisateur déjà pris")
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


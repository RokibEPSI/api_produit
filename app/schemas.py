from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    created_at: str
    price: str
    description: str
    color: str
    stock: str
    order_id: int

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True

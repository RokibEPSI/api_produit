from app.schemas import ProductCreate, ProductOut, Token, UserOut

def test_product_create_schema():
    product = ProductCreate(
        name="Café latte",
        created_at="2024-01-01T10:00:00",
        price="3.50",
        description="Boisson chaude",
        color="brun",
        stock="100",
        order_id=1
    )
    assert product.name == "Café latte"
    assert product.price == "3.50"

def test_token_schema():
    token = Token(access_token="abc123", token_type="bearer")
    assert token.access_token == "abc123"
    assert token.token_type == "bearer"

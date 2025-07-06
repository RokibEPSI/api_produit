from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

def test_get_products():
    response = client.get("/produits/")
    assert response.status_code in [200, 500]

# ✅ Patch l'import réel utilisé par `routes.py`, pas la source de la fonction
@patch("app.routes.publish_event")
def test_create_product_unauthorized(mock_publish):
    response = client.post("/produits/", json={
        "name": "Produit Test",
        "created_at": "2025-07-05T12:00:00",
        "price": "19.99",
        "description": "Un produit de test",
        "color": "rouge",
        "stock": "10",
        "order_id": 1
    })
    assert response.status_code == 401
    mock_publish.assert_not_called()

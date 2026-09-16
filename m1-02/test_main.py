
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_item():
    create_resp = client.post("/items", json={"name": "Mouse", "price": 9.99})
    assert create_resp.status_code == 201
    item_id = create_resp.json()["id"]

    get_resp = client.get(f"/items/{item_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["name"] == "Mouse"


def test_get_missing_item_returns_404():
    response = client.get("/items/9999")
    assert response.status_code == 404


def test_create_item_rejects_invalid_body():
    # missing required field "name" -> Pydantic validation error -> 422
    response = client.post("/items", json={"price": 5.0})
    assert response.status_code == 422
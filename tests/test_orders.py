from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_create_and_get_order():
    payload = {"item": "Brake Pads", "quantity": 2}
    r = client.post("/orders", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["item"] == "Brake Pads"
    order_id = data["id"]
    r2 = client.get(f"/orders/{order_id}")
    assert r2.status_code == 200
    data2 = r2.json()
    assert data2["id"] == order_id
def test_list_orders():
    r = client.get("/orders")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

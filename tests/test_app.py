from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200

def test_process():
    res = client.post("/process", json={"key": "value"})
    assert res.status_code == 200

def test_fail():
    res = client.get("/fail")
    assert res.status_code == 500
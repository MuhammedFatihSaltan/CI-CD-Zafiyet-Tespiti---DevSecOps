from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """/health endpointinin 200 OK ve doğru JSON döndürdüğünü test eder."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Service is running securely."}
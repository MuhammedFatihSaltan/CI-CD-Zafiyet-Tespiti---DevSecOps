from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DevSecOps Pipeline Aktif ve Calisiyor!"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_analyze_network_logs():
    """
    Pandas ile entegre edilen Kaggle veri seti uç noktasının testi.
    Sunucuya 200 OK yanıtı döndüğünü ve JSON formatında çalıştığını doğrular.
    """
    response = client.get("/analyze-logs")
    assert response.status_code == 200
    
    # JSON yanıtının içinde belirli anahtarların (keys) olup olmadığını kontrol et
    data = response.json()
    assert "total_analyzed_logs" in data
    assert "threats_found" in data
    assert "high_risk_logs" in data
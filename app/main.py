import hashlib
from fastapi import FastAPI

app = FastAPI(
    title="SecureFlow Demo API",
    description="DevSecOps pipeline testleri için minimal hedef uygulama.",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    """Sistemin ayakta olup olmadığını kontrol eden endpoint."""
    return {"status": "ok", "message": "Service is running securely."}

@app.get("/insecure-hash")
def generate_hash(data: str):
    """Bilinçli Zafiyet: Zayıf ve kırılmış MD5 algoritması kullanımı."""
    # Semgrep bu satırı tehlikeli bulup pipeline'ı durdurmalıdır!
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    return {"hash": md5_hash}
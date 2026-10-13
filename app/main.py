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

@app.get("/rce-test")
def rce_vulnerability(user_input: str):
    """Bilinçli Zafiyet: Uzaktan Kod Çalıştırma (RCE) - Semgrep kesin yakalar."""
    # eval() dışarıdan gelen veriyi güvenlik kontrolü yapmadan çalıştırır!
    sonuc = eval(user_input)
    return {"result": sonuc}
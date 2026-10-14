from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI(title="SecureFlow Demo API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "DevSecOps Pipeline Aktif ve Calisiyor!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/analyze-logs")
def analyze_network_logs():
    """
    Kaggle ağ trafiği veri setini (CSV) okur, 
    sadece saldırı riski yüksek (Malicious) olan logları filtreleyip döndürür.
    """
    # CSV dosyasının bulunduğu yolu belirliyoruz
    file_path = os.path.join(os.path.dirname(__file__), "network_logs.csv")
    
    try:
        # Pandas ile veri setini okuyoruz
        df = pd.read_csv(file_path)
        
        # Sadece 'Malicious' (Zararlı/Saldırı) olan trafikleri filtreliyoruz
        threats = df[df['status'] == 'Malicious']
        
        # Sonuçları JSON formatına çevirip döndürüyoruz
        return {
            "total_analyzed_logs": len(df),
            "threats_found": len(threats),
            "high_risk_logs": threats.to_dict(orient="records")
        }
    except Exception as e:
        return {"error": f"Veri seti islenirken hata olustu: {str(e)}"}
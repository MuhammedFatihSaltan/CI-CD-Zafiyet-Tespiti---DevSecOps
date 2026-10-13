# Güvenli ve küçük bir temel imaj seçiyoruz
FROM python:3.11-slim

# Root olmayan yetkisiz bir kullanıcı oluştur (Güvenlik gereksinimi)
RUN useradd -m -s /bin/bash appuser

WORKDIR /app

# Sadece gereksinimleri kopyalayıp kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Dosya sahipliğini yetkisiz kullanıcıya ver
RUN chown -R appuser:appuser /app

# Uygulamayı root olmayan kullanıcıyla çalıştır
USER appuser

EXPOSE 8000

# Uygulamayı başlat
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# SecureFlow Tehdit Modeli (Taslak)

Bu doküman, CI/CD güvenlik hattımızın korumaya çalıştığı varlıkları ve olası tehditleri tanımlar.

## Varlıklar (Assets)
1.  **Kaynak Kod:** Projenin iş mantığı ve mimarisi.
2.  **Sırlar (Secrets):** API anahtarları, veritabanı şifreleri, CI/CD ortam değişkenleri.
3.  **Bağımlılıklar (Dependencies):** Dışarıdan dahil edilen kütüphane ve paketler.
4.  **Konteyner İmajları:** Uygulamanın çalışacağı temel sistem ve paketlenmiş hali.
5.  **Derleme Çıktıları (Artifacts):** GitHub Actions tarafından üretilen raporlar (SARIF, JSON).

## Güven Sınırları (Trust Boundaries)
-   **Yerel Geliştirme Ortamı:** Geliştiricinin kendi bilgisayarı (Düşük güven).
-   **Kaynak Kod Deposu (GitHub):** Kodun ve geçmişin tutulduğu alan (Orta güven).
-   **CI/CD Pipeline (GitHub Actions):** Taramaların ve derlemelerin çalıştığı geçici ortam (Yüksek güven).

## Temel Tehdit Senaryoları
1.  **Yanlışlıkla Sır Sızıntısı:** Geliştiricinin `.env` dosyasını veya hardcoded bir API anahtarını commitlemesi.
    *   *Önlem:* CI hattında Gitleaks çalıştırılması ve Pull Request birleştirilmeden önce reddedilmesi.
2.  **Zafiyetli Kütüphane Kullanımı:** Kritik CVE (Ortak Zafiyetler ve Açıklar) barındıran bir modülün projeye eklenmesi.
    *   *Önlem:* Trivy ile bağımlılık taraması yapılıp, kritik seviyede eşik aşıldığında derlemenin durdurulması.
3.  **Riskli Docker Yapılandırması:** İmajın root kullanıcısıyla çalıştırılması veya gereksiz işletim sistemi paketleri içermesi.
    *   *Önlem:* Trivy ve Dockerfile linting araçlarıyla build sonrası denetim yapılması.
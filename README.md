# SecureFlow - DevSecOps CI/CD Security Gate

Automated Security Scanning and Policy Enforcement for CI/CD Pipelines.

## Problem
Geliştiriciler farkında olmadan API anahtarları, parolalar veya güvenlik açığı barındıran bağımlılıkları kaynak koda dahil edebilirler. Bu risklerin üretim ortamına taşınmadan önce, geliştirme sürecinin en erken aşamasında tespit edilmesi gereklidir.

## Çözüm
SecureFlow, GitHub Actions üzerinde çalışan otomatik bir DevSecOps hattıdır. Kod depoya gönderildiğinde; secret sızıntıları, statik kod zafiyetleri (SAST) ve bağımlılık/konteyner açıkları otomatik olarak taranır. Belirlenen "Security Gate" eşikleri aşıldığında pipeline durdurulur ve geliştiriciye net bir geri bildirim sunulur.

## MVP Kapsamı
- GitHub Actions ile otomatik CI/CD iş akışları
- Gitleaks ile Secret Scanning
- SAST (Statik Kod Analizi)
- Trivy ile Bağımlılık ve Docker İmaj Taraması
- Güvenlik Kapısı (Security Gate) mekanizması
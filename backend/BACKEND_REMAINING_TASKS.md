# Backend Kalan Isler (Durum Dosyasi)

Bu dosya, projede backend tarafinda kalan isleri sirasiyla bitirmek icin hazirlandi.

## 1) Kritik Eksik: Veritabani Baglantisi

Su an migration uyarisinin ana nedeni budur.

- [ ] PostgreSQL instance hazirla (lokal Docker veya cloud)
- [ ] `.env` dosyasi olustur (`.env.example` baz alinacak)
- [ ] Asagidaki degiskenleri doldur:
  - `POSTGRES_HOST`
  - `POSTGRES_PORT`
  - `POSTGRES_DB`
  - `POSTGRES_USER`
  - `POSTGRES_PASSWORD`
  - `DJANGO_SECRET_KEY`
  - `DJANGO_ALLOWED_HOSTS`
  - `CORS_ALLOWED_ORIGINS`

## 2) Kurulum Sonrasi Zorunlu Komutlar

- [ ] `.\.venv\Scripts\python.exe manage.py migrate`
- [ ] `.\.venv\Scripts\python.exe manage.py seed_demo_data` (opsiyonel ama onerilir)
- [ ] `.\.venv\Scripts\python.exe manage.py runserver`
- [ ] `.\.venv\Scripts\python.exe manage.py test`

## 3) API Saglik Kontrolu (Hizli)

- [ ] `GET /api/pages/home/` -> 200
- [ ] `GET /api/services/` -> 200
- [ ] `GET /api/blog/` -> 200
- [ ] `GET /api/projects/` -> 200
- [ ] `GET /api/contact/` -> 200
- [ ] `POST /api/auth/token/` -> 200
- [ ] `GET /api/me/policies/` (Bearer ile) -> 200

## 4) Frontend'e Teslim Edilecekler

- [x] `BACKEND_HANDOFF.md` hazir
- [x] `POSTMAN_TEST_GUIDE.md` hazir
- [ ] (Opsiyonel) Postman Collection JSON export edilip paylasilacak
- [ ] Frontend ile son endpoint/alan adi onayi alinacak

## 5) DevOps / Docker Tarafi

- [x] `Dockerfile` mevcut
- [x] `docker-compose.yml` mevcut
- [ ] Makinede Docker kurulu oldugunu dogrula
- [ ] `docker compose up --build` ile ayaga kaldirma testi yap
- [ ] Container loglarinda migrate + seed + gunicorn akisini dogrula

## 6) Sunum Oncesi Kontrol Listesi

- [ ] Tum migrationlar uygulanmis
- [ ] En az 1 demo kullanici ile login test edilmis
- [ ] 5 private endpoint canli test edilmis
- [ ] Contact form verisi DB'ye dusuyor
- [ ] 24 testin tamami geciyor
- [ ] Frontend entegrasyonunda endpoint mismatch yok

## 7) Mevcut Durum Ozeti (Bugun)

- [x] Moduler Django API tamam
- [x] PostgreSQL uyumlu ayarlar tamam
- [x] JWT auth tamam
- [x] Public + private endpointler tamam
- [x] Unit/API testleri 24 adet ve yesil
- [ ] Gercek PostgreSQL baglantisi ve migrate adimi bekleniyor


# Backend Handoff (Frontend Entegrasyon Rehberi)

Bu dokuman, frontend tarafinin backend API'lere hatasiz baglanabilmesi icin hazirlanmistir.

## 1) Calistirma Bilgisi

- Backend base URL: `http://127.0.0.1:8000`
- API base URL: `http://127.0.0.1:8000/api`
- Lokal backend komutu:
  - `.\.venv\Scripts\python.exe manage.py runserver`

## 2) Authentication (JWT)

### Register
- `POST /api/auth/register/`
- Body:
```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "StrongPass123!",
  "first_name": "New",
  "last_name": "User"
}
```

### Login
- `POST /api/auth/token/`
- Body:
```json
{
  "username": "demo",
  "password": "Demo12345!"
}
```
- Response:
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

### Refresh
- `POST /api/auth/token/refresh/`
- Body:
```json
{
  "refresh": "<refresh_token>"
}
```

### Protected Endpoint Header
- Tum korumali endpointlerde su header zorunlu:
  - `Authorization: Bearer <access_token>`

## 3) Public Endpointler (Login gerekmez)

### Static sayfalar
- `GET /api/pages/home/`
- `GET /api/pages/home-2/`
- `GET /api/pages/about/`

Response (ornek):
```json
{
  "slug": "home",
  "meta_title": "Insucom - Ana Sayfa",
  "hero_headline": "Guvenli Yarinlar Icin Sigorta Ortaginiz",
  "hero_subheadline": "Arac, konut ve saglik cozumlerinde yaninizdayiz.",
  "intro": "Seffaf fiyatlandirma ve hizli police surecleri.",
  "updated_at": "2026-04-21T12:00:00Z",
  "sections": [
    {
      "key": "hero-cta",
      "title": "Hemen Teklif Alin",
      "body": "Uzman ekibimiz 7/24 destek sunar.",
      "image_path": "./assets/img/logo.svg",
      "sort_order": 1
    }
  ],
  "statistics": []
}
```

### Services
- `GET /api/services/`
- `GET /api/services/<slug>/`

### Blog
- `GET /api/blog/`
- `GET /api/blog/<slug>/`

### Projects
- `GET /api/projects/`
- `GET /api/projects/<slug>/`

### FAQ
- `GET /api/faq/`

### Contact sayfasi + form
- `GET /api/contact/`
- `POST /api/contact/messages/`

Contact message body:
```json
{
  "name": "Ali Veli",
  "email": "ali@example.com",
  "phone": "+90 555 111 22 33",
  "message": "Merhaba, teklif alabilir miyim?",
  "source_page": "contact.html"
}
```

## 4) Private Endpointler (Login gerekli)

- `GET /api/me/policies/`  -> Policelerim
- `GET /api/me/quotes/`    -> Tekliflerim
- `GET /api/me/claims/`    -> Hasar Kayitlarim
- `GET /api/me/payments/`  -> Odemelerim
- `GET /api/me/alerts/`    -> Bildirimlerim

Not: Kullanici sadece kendi verisini gorur.

## 5) Frontend Entegrasyon Kurallari

- Slug detay sayfalarinda route param olarak kullanilmali:
  - `/services/[slug]` -> `GET /api/services/<slug>/`
  - `/blog/[slug]` -> `GET /api/blog/<slug>/`
  - `/projects/[slug]` -> `GET /api/projects/<slug>/`
- Date/number alanlarini frontend formatlamali (backend ham deger doner).
- `4xx` donuslerinde body okunup hata mesaji gosterilmeli.

## 6) HTTP Status Beklentileri

- `200`: basarili GET
- `201`: basarili create (`/api/contact/messages/`, `/api/auth/register/`)
- `400`: validation hatasi (eksik/yanlis alan)
- `401`: token yok/invalid/expired
- `404`: slug bulunamadi

## 7) Axios Ornekleri

### Public request
```ts
import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

const res = await api.get("/services/");
```

### Login + protected request
```ts
const login = await api.post("/auth/token/", {
  username: "demo",
  password: "Demo12345!",
});

const access = login.data.access;

const myPolicies = await api.get("/me/policies/", {
  headers: { Authorization: `Bearer ${access}` },
});
```

## 8) Ortam ve CORS

- Backend CORS localhost frontend icin acik:
  - `http://localhost:3000`
- Farkli port/domain kullanilacaksa backend `.env` icinde `CORS_ALLOWED_ORIGINS` guncellenmeli.

## 9) Gelistirme Sirasi (Frontend icin onerilen)

1. Public sayfalari bagla (`pages`, `services`, `blog`, `projects`, `faq`, `contact`)
2. Contact form POST akisini tamamla
3. Login ekranini bagla
4. Token saklama + refresh stratejisi ekle
5. 5 private sayfayi bagla (`/me/*`)

## 10) Hata Yapmamak Icin Kisa Checklist

- [ ] Base URL dogru mu? (`/api` unutulmasin)
- [ ] Slug endpointleri dogru route ile eslendi mi?
- [ ] Protected endpointlerde Bearer token var mi?
- [ ] 401 olunca login'e yonlendirme var mi?
- [ ] Form POST body alan adlari birebir dogru mu? (`name`, `email`, `phone`, `message`, `source_page`)
- [ ] Loading + error UI durumlari eklendi mi?

## 11) HTML Dosyasi -> Endpoint Esleme Tablosu

Bu tablo frontend tarafinin birebir hangi sayfada hangi endpoint'i cagirmasi gerektigini netlestirir.

- `index.html` -> `GET /api/pages/home/` + ana listeler icin `services/blog/projects` kisa listing
- `index-2.html` -> `GET /api/pages/home-2/`
- `about.html` -> `GET /api/pages/about/`
- `services.html` -> `GET /api/services/`
- `service-details.html` -> `GET /api/services/<slug>/`
- `blogs.html` -> `GET /api/blog/`
- `blog-details.html` -> `GET /api/blog/<slug>/`
- `project.html` -> `GET /api/projects/`
- `project-details.html` -> `GET /api/projects/<slug>/`
- `faq.html` -> `GET /api/faq/`
- `contact.html` -> `GET /api/contact/` + `POST /api/contact/messages/`

### Login sonrasi ozel sayfalar (frontend tarafinda yeni route)

- `/account/policies` -> `GET /api/me/policies/`
- `/account/quotes` -> `GET /api/me/quotes/`
- `/account/claims` -> `GET /api/me/claims/`
- `/account/payments` -> `GET /api/me/payments/`
- `/account/alerts` -> `GET /api/me/alerts/`

## 12) Frontend Data Contract (Alan Bazli)

Bu kisimda kritik alan isimleri birebir yazilmistir. Frontend bu isimleri oldugu gibi kullanmalidir.

### Services list item
- `id`, `title`, `slug`, `short_description`, `icon_path`, `icon_url`, `category`, `sort_order`, `updated_at`

### Service detail
- list alanlari + `body`

### Blog list item
- `id`, `title`, `slug`, `excerpt`, `cover_image_path`, `cover_image_url`, `author_display_name`, `published_at`, `category`, `updated_at`

### Blog detail
- list alanlari + `body`

### Project list item
- `id`, `title`, `slug`, `summary`, `cover_image_path`, `cover_image_url`, `client_name`, `completed_on`, `category`, `sort_order`, `updated_at`

### Project detail
- list alanlari + `body`

### Coverage map + contract
- `GET /api/pages/coverage-map/`
- Her sayfa icin su alanlar gelir:
  - `html`
  - `model_source`
  - `api`
  - `contract` (frontendin zorunlu bekleyecegi field listesi)
  - `mock_data_check` (`not_null`, `sample_values`, uygun sayfada `html_static_match`)

### Contact page
- `profile.intro_kicker`
- `profile.intro_headline`
- `profile.intro_body`
- `profile.map_embed_url`
- `cards[]`: `kind`, `title_label`, `line_primary`, `line_secondary`, `sort_order`

## 13) Backend Degisiklik Kurali (Frontend'i Kirmamak Icin)

- Backend tarafi endpoint pathlerini ve alan adlarini degistirmeden ilerlemelidir.
- Degisiklik zorunluysa frontend ekibine once bildirilip versiyonlama yapilmalidir.
- Frontend tamamlanana kadar `seed_demo_data` sadece veri icerigi gunceller, field adlarini degistirmez.

## 14) Frontend Icin Hazir Demo Hesap ve Test Verisi

- Demo login:
  - `username`: `demo`
  - `password`: `Demo12345!`
- Demo data yukleme komutu:
  - `.\.venv\Scripts\python.exe manage.py seed_demo_data`
- Frontend entegrasyonda once bu hesapla login test edilmelidir.

## 15) Ortam Senaryolari (Lokal Python vs Docker)

### A) Lokal Python (runserver)
- Backend:
  - `.\.venv\Scripts\python.exe manage.py runserver`
- API base URL:
  - `http://127.0.0.1:8000/api`
- DB:
  - `.env` degerlerine gore (Azure/Postgres veya local)

### B) Docker Compose
- Komut:
  - `docker compose up --build`
- API base URL:
  - `http://127.0.0.1:8000/api`
- DB:
  - Docker icindeki `db` servisi (`POSTGRES_HOST=db`)
- Not:
  - Docker local postgres SSL desteklemedigi icin compose tarafinda `POSTGRES_SSLMODE=disable` ayarlidir.

## 16) Frontend Entegrasyonunda Kritik Notlar

- Tum endpointlerde sonda `/` kullanin (`/api/services/` gibi).
- `GET /api/pages/home/` gibi public endpointlerde token gondermek zorunlu degildir.
- Sadece `/api/me/*` endpointleri token ister.
- Token suresi dolarsa:
  - `POST /api/auth/token/refresh/` ile yeni access alin.
- `POST /api/contact/messages/` body alan adlari sabittir:
  - `name`, `email`, `message`

## 17) Frontend Teslim Oncesi 10 Dakika Smoke Plani

1. `POST /api/auth/token/` -> 200, `access` al
2. `GET /api/pages/home/` -> 200
3. `GET /api/services/` -> 200
4. `GET /api/blog/` -> 200
5. `GET /api/projects/` -> 200
6. `GET /api/faq/` -> 200
7. `GET /api/contact/` -> 200
8. `POST /api/contact/messages/` -> 201
9. `GET /api/me/policies/` -> 200 (Bearer)
10. `GET /api/me/quotes/`, `/claims/`, `/payments/`, `/alerts/` -> 200 (Bearer)


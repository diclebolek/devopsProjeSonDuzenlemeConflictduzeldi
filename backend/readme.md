## Backend Teknik Teslimat Raporu

Bu belge, sigorta temasi backend tesliminin teknik ozetidir.

### Teknoloji Yigini

- Django REST API
- PostgreSQL (Azure uyumlu baglanti)
- Docker (backend container calistirma senaryosu)
- JWT (SimpleJWT)
- Unit test altyapisi (Django TestCase + DRF APIClient)

### 11 Ana Sayfa - Veritabani Besleme Durumu

Asagidaki 11 sayfa PostgreSQL kaynakli modellerden beslenir:

- `index.html` -> `StaticPage`, `PageSection`, `SiteSetting`
- `index-2.html` -> `StaticPage`, `PageSection`, `SiteSetting`
- `about.html` -> `StaticPage`, `PageStatistic`, `SiteSetting`
- `services.html` -> `Service`, `ServiceCategory`
- `service-details.html` -> `Service`, `ServiceFeature`, `ServiceCategory`
- `project.html` -> `Project`, `ProjectCategory`
- `project-details.html` -> `Project`, `ProjectMeta`, `ProjectCategory`
- `blogs.html` -> `BlogPost`, `BlogCategory`
- `blog-details.html` -> `BlogPost`, `BlogComment`, `BlogCategory`
- `faq.html` -> `FAQEntry`
- `contact.html` -> `ContactSiteProfile`, `ContactCard`, `ContactMessage`

### Contract Endpoint (Coverage Map)

`GET /api/pages/coverage-map/` endpointi su bilgileri JSON olarak verir:

- Sayfa bazli model ve API eslemesi
- Frontend icin zorunlu field checklist (contract)
- Mock data kontrolu (`not_null`)
- Ornek statik deger ortusmesi kontrolu
  - `project-details.html` icin `45,000$` eslesmesi dahil

Bu endpoint frontend ekibinin "hangi sayfada hangi JSON alanlarini beklemeliyim?" sorusuna dogrudan cevap verir.

### Dinamik Gorsel URL Sozlesmesi

Asagidaki serializerlarda statik yolun yaninda dinamik URL alani da sunulur:

- `PageSectionSerializer` -> `image_url`
- `ServiceListSerializer`, `ServiceDetailSerializer` -> `icon_url`
- `ProjectListSerializer`, `ProjectDetailSerializer` -> `cover_image_url`
- `BlogPostListSerializer`, `BlogPostDetailSerializer` -> `cover_image_url`

### Form-API Eslesmesi

Hoca HTML paketindeki kritik formlar backend alanlariyla hizalanmistir:

- `name`
- `email`
- `phone`
- `message`
- `source_page`

Ana hedef endpoint: `POST /api/contact/messages/`

### Code First ve Sinif Tasarimi

Modelleme Code First prensibine gore yapilmistir. Eklenen temel sinif/ozellikler:

- `SiteSetting`
- `SocialLink`
- `ServiceFeature`
- `ProjectMeta`
- `BlogComment`

Property method ornekleri:

- `SiteSetting.primary_contact`
- `Service.feature_count`
- `Project.budget_display`
- `BlogPost.approved_comment_count`

### Azure ve PostgreSQL Uyumu

`config/settings.py` davrani�i:

- Test komutu (`manage.py test`) icin in-memory SQLite
- Runtime'da `POSTGRES_HOST` veya `AZURE_POSTGRES_HOST` varsa PostgreSQL
- Azure host/port/user env fallback destegi

### JWT Hardening

`SIMPLE_JWT` konfigurasyonuna guclu `SIGNING_KEY` guard eklendi:

- `JWT_SIGNING_KEY` env degeri 32+ karakter ise kullanilir
- Aksi halde guclu fallback key devreye girer

Bu sayede kisa HMAC key kaynakli JWT warningleri engellenir.

### Test Sonucu

Guncel durum:

- Toplam test: `51`
- Sonuc: `OK`
- Kritik API ve model birimleri kapsanmistir

### Teslim Notu

Migration dosyalari uretilmis durumdadir. Yeni ortama kurulumda standart adimlar:

1. `pip install -r requirements.txt`
2. `python manage.py migrate`
3. `python manage.py test`

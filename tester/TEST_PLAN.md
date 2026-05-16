# SigortaWebSitesi - Kapsamlı Test Planı Dokümanı

## 1. Amaç ve Kapsam
Bu dokümanın amacı, **SigortaWebSitesi** projesinin (Django REST API backend ve Next.js frontend) kalite güvence (QA) süreçlerini planlamak, yönetmek ve standartlaştırmaktır. Test süreci; birim, entegrasyon ve kullanıcı arayüzü (E2E) seviyelerinde projenin istenen gereksinimleri karşıladığını doğrulamayı hedefler.

**Kapsama Dahil Olanlar:**
* Backend REST API uç noktalarının (endpoints) doğruluğu ve güvenliği.
* Veritabanı entegrasyonlarının (CRUD işlemleri) tutarlılığı.
* Frontend (Next.js) arayüzünün işlevselliği ve kullanıcı deneyimi.
* Form validasyonları, yetkilendirme (Auth) ve hata yönetimi süreçleri.

**Kapsam Dışı Olanlar:**
* Sunucu donanım performans testleri (Load/Stress Testing bu fazda hariç tutulmuştur).

## 2. Test Ortamı ve Araçlar
Testlerin izole ve güvenilir bir şekilde koşulabilmesi için aşağıdaki araçlar ve ortamlar kullanılacaktır:

* **Backend Entegrasyon Testleri:** `pytest` ve `pytest-django`
* **API Testleri (Manuel/Yarı Otomatik):** Postman (Mevcut `POSTMAN_TEST_GUIDE.md` referans alınacaktır)
* **Uçtan Uca (E2E) UI Testleri:** Selenium WebDriver (Python)
* **Sürekli Entegrasyon (CI):** Azure DevOps Pipelines (`azure-pipelines.yml` içerisine `Test` aşaması olarak entegre edilecektir)
* **Test Veritabanı:** Docker üzerinden ayağa kaldırılan izole PostgreSQL/SQLite instance'ı.

## 3. Test Stratejisi ve Seviyeleri

### 3.1. Entegrasyon Testleri (Integration Testing)
Backend ile veritabanı veya Frontend ile Backend arasındaki iletişimin test edilmesidir.
* **Odak:** API yanıt kodları (200, 201, 400, 401, 404), veri formatları (JSON doğruluğu) ve yetki kontrolleri (Token bazlı erişim).
* **Kabul Kriteri:** Tüm API endpoint'lerinin doğru payload ile başarılı yanıt dönmesi, hatalı payload ile uygun hata mesajlarını dönmesi.

### 3.2. Uçtan Uca Testler (E2E - Selenium)
Gerçek bir kullanıcının tarayıcı (Chrome/Firefox) üzerindeki davranışlarının simüle edilmesidir. En az 20 ana senaryo (Test Case) otomatize edilecektir.

## 4. Selenium E2E Test Senaryoları Kapsamı (20 Adet) /// Bu kısım yazılan selenium testlerine göre değiştirilecektir
Uçtan uca testler aşağıdaki modüllere ayrılarak uygulanacaktır:

**Modül 1: Kimlik Doğrulama (Authentication)**
1. Başarılı kullanıcı girişi (Login)
2. Hatalı şifre ile giriş denemesi ve hata mesajı kontrolü
3. Yeni kullanıcı kaydı (Register)
4. Boş alanlarla kayıt olma denemesi ve form validasyonu
5. Sisteme giriş sonrası güvenli çıkış (Logout) işlemi

**Modül 2: Temel Gezinme (Navigation & CMS)**
6. Anasayfa modüllerinin ve banner'ların eksiksiz yüklenmesi
7. Hakkımızda (About) sayfasına erişim kontrolü
8. Sıkça Sorulan Sorular (FAQ) accordion menülerinin açılıp kapanma testi
9. Blog sayfasında gönderilerin listelenmesi
10. Tıklanan bir blog postunun detay sayfasına (slug) başarılı yönlendirme

**Modül 3: Sigortacılık İşlemleri (Core Business)**
11. Servis (Sigorta) detay sayfalarının görüntülenmesi
12. Sigorta Poliçesi Teklif Alma (Quote) formunun başarılı doldurulması
13. Teklif formunda zorunlu alan validasyonu
14. Hasar talebi (Claim) formunun doldurulup gönderilmesi
15. Kullanıcı panelinde (Account) aktif poliçelerin listelenmesi

**Modül 4: İletişim ve Kullanıcı Bildirimleri**
16. İletişim (Contact) formunun başarılı bir şekilde gönderilmesi
17. İletişim formunda hatalı e-posta formatı validasyonu
18. Sistem içi bildirimlerin/uyarıların (Alerts) UI üzerinde görünürlüğü
19. Kullanıcı ödeme geçmişi (Payments) sayfasının yüklenmesi
20. Admin (/admin) paneline giriş ekranının erişilebilirliği ve yetkisiz girişi reddetme

## 5. Hata (Bug) Yönetimi
Testler sırasında tespit edilen hatalar aşağıdaki formatta raporlanacaktır:
1. **Hata Başlığı:** [Modül] - Kısa açıklama (Örn: [Auth] - Yanlış şifre girildiğinde hata mesajı çıkmıyor)
2. **Yeniden Üretme Adımları (Steps to Reproduce):** Hatanın nasıl alınacağına dair adım adım bilgi.
3. **Beklenen Sonuç:** Sistemin normalde vermesi gereken tepki.
4. **Alınan Sonuç:** Sistemin mevcut hatalı tepkisi.
5. **Ekler:** Ekran görüntüsü veya log kayıtları.

## 6. Teslimat ve CI/CD Entegrasyonu
Yazılan tüm Selenium ve pytest betikleri projeye dahil edildikten sonra, Azure DevOps Pipeline yapılandırmasına (`azure-pipelines.yml`) bir test adımı eklenecektir. Kod repoya her push edildiğinde testler otomatik çalışacak ve testleri geçemeyen kodlar sunucuya deploy edilmeyecektir.
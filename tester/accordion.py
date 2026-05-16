import pytest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestGeneralPages:
    def setup_method(self):
        # Her testten önce tarayıcıyı başlat
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "http://localhost:3000"

    def teardown_method(self):
        # Her testten sonra tarayıcıyı kapat
        self.driver.quit()

    def show_virtual_cursor(self, element):
        """Selenium'un sanal faresinin nereye gittiğini gösteren kırmızı bir lazer nokta çizer"""
        script = """
        var ele = arguments[0];
        // Elementin ekrandaki koordinatlarını (X ve Y) ve boyutunu al
        var rect = ele.getBoundingClientRect();
        var x = rect.left + (rect.width / 2);
        var y = rect.top + (rect.height / 2);
        
        // Ekranda önceden oluşturduğumuz bir sanal imlecimiz var mı bak
        var cursor = document.getElementById('selenium-cursor');
        if (!cursor) {
            // Yoksa yeni bir kırmızı nokta (div) yarat
            cursor = document.createElement('div');
            cursor.id = 'selenium-cursor';
            cursor.style.width = '20px';
            cursor.style.height = '20px';
            cursor.style.borderRadius = '50%'; // Yuvarlak yapar
            cursor.style.backgroundColor = 'rgba(255, 0, 0, 0.8)'; // Kırmızı renk
            cursor.style.position = 'fixed'; // Ekrana sabitle
            cursor.style.zIndex = '999999'; // Her şeyin en üstünde dursun
            cursor.style.pointerEvents = 'none'; // Tıklamaları engellemesin
            cursor.style.transition = 'all 0.3s ease'; // Ekranda süzülerek gitsin
            document.body.appendChild(cursor);
        }
        
        // Kırmızı noktayı Selenium'un hedeflediği elementin tam ortasına gönder
        cursor.style.left = (x - 10) + 'px';
        cursor.style.top = (y - 10) + 'px';
        """
        self.driver.execute_script(script, element)
        time.sleep(0.5)

    # TEST 34: Orijinal Footer (Footer.tsx) İç Link (Navigation) Testi
    def test_footer_main_internal_links(self):
        self.driver.get(self.base_url)

        # 1. Koca footer'ı DEĞİL, doğrudan hedef linki buluyoruz
        about_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//footer//div[contains(@class, 'quick-links')]//a[@href='/about']"))
        )
        
        # 2. Sadece o linki ekranın tam ortasına getiriyoruz (Ekran dışı hatasını engeller)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", about_link)
        time.sleep(1)

        # 3. Görsel animasyon ve tıklama
        self.show_virtual_cursor(about_link)
        actions = ActionChains(self.driver)
        actions.move_to_element(about_link).perform()
        time.sleep(0.5)
        
        actions.click().perform()
        time.sleep(1)

        # 4. Yönlendirme doğrulama
        WebDriverWait(self.driver, 10).until(EC.url_contains("/about"))
        assert "/about" in self.driver.current_url


    # TEST 37: Home-2 Footer "Services" Linkleri Testi
    def test_home2_footer_services_links(self):
        self.driver.get(f"{self.base_url}/home-2")
        actions = ActionChains(self.driver)

        # 1. 'Services' başlığı altındaki 'Software development' linkini bul
        software_dev_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//footer//a[contains(text(), 'Software development')]"))
        )
        
        # 2. Elementi ortala ve fareyi üzerine götür
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", software_dev_link)
        time.sleep(0.5)
        self.show_virtual_cursor(software_dev_link)
        actions.move_to_element(software_dev_link).perform()
        time.sleep(0.5)

        # 3. Tıkla ve yönlendirmeyi doğrula (Projenizin link yapısına göre güncellenebilir)
        actions.click().perform()
        WebDriverWait(self.driver, 10).until(EC.url_contains("/services"))
        assert "/services" in self.driver.current_url


    # TEST 38: Home-2 Footer "Recent Work" Linkleri Testi
    def test_home2_footer_recent_work_links(self):
        self.driver.get(f"{self.base_url}/home-2")
        actions = ActionChains(self.driver)

        # 1. 'Recent Work' altındaki 'Risk Assessment' linkini bul
        risk_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//footer//a[contains(text(), 'Risk Assessment')]"))
        )
        
        # 2. Ortala ve fareyi getir
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", risk_link)
        time.sleep(0.5)
        self.show_virtual_cursor(risk_link)
        actions.move_to_element(risk_link).perform()
        time.sleep(0.5)

        # 3. Tıkla ve doğrula
        actions.click().perform()
        WebDriverWait(self.driver, 10).until(EC.url_contains("/services/risk-assessment") or EC.url_contains("/projects"))
        assert "risk-assessment" in self.driver.current_url or "project" in self.driver.current_url


    # TEST 39: Home-2 Footer "All Links" Kolonu Testi
    def test_home2_footer_all_links(self):
        self.driver.get(f"{self.base_url}/home-2")
        actions = ActionChains(self.driver)

        # 1. 'All Links' altındaki 'Insure Pro' linkini hedefle
        insure_pro_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//footer//a[contains(text(), 'Insure Pro')]"))
        )
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", insure_pro_link)
        time.sleep(0.5)
        self.show_virtual_cursor(insure_pro_link)
        actions.move_to_element(insure_pro_link).perform()
        time.sleep(0.5)

        actions.click().perform()
        time.sleep(1)
        # Geliştiricinin bu linki nereye yönlendirdiğine bağlı olarak assertion yazılır
        assert self.driver.current_url != f"{self.base_url}/home-2"


    # TEST 40: Home-2 Yeşil Banner "Discover More" Butonu Testi
    def test_home2_banner_discover_more(self):
        self.driver.get(f"{self.base_url}/home-2")
        actions = ActionChains(self.driver)

        # 1. Görseldeki en altta duran büyük yeşil bar içindeki 'Discover More' butonunu bul
        discover_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Discover More')]/parent::a | //a[contains(., 'Discover More')]"))
        )
        
        # 2. Elementi ekrana getir ve fare şovunu yap
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", discover_btn)
        time.sleep(0.5)
        self.show_virtual_cursor(discover_btn)
        actions.move_to_element(discover_btn).perform()
        time.sleep(0.5)

        # 3. Tıkla ve anasayfadan başka bir yere (muhtemelen /about veya /services) gittiğini doğrula
        actions.click().perform()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != f"{self.base_url}/home-2")
        assert f"{self.base_url}/home-2" != self.driver.current_url


    # TEST 41: Home-2 Üst Sağ Sosyal Medya İkonları Hover Testi
    def test_home2_social_media_hover(self):
        self.driver.get(f"{self.base_url}/home-2")
        actions = ActionChains(self.driver)

        # 1. Sağ üst köşede yan yana duran yuvarlak sosyal medya ikon paketini bul (Twitter, Facebook vb.)
        # href içinde twitter geçen ilk <a> etiketini yakalayalım
        twitter_icon = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'twitter.com') or contains(@href, 'x.com')]"))
        )
        
        # 2. Yukarı kaydırıp tam ikonun üstüne odaklanalım
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", twitter_icon)
        time.sleep(0.5)
        
        # 3. Kırmızı lazeri ikona kilitle ve fareyi üzerine getir
        self.show_virtual_cursor(twitter_icon)
        actions.move_to_element(twitter_icon).perform()
        time.sleep(1) # Hover etkisini (varsa renk değişimini) izlemek için bekliyoruz

        # 4. Sosyal medya linklerinin dışarı açılması gerektiği için target='_blank' kontrolü yapalım
        assert twitter_icon.get_attribute("target") == "_blank", "HATA: Sosyal medya linki yeni sekmede (_blank) açılmıyor!"


    # TEST 36: Footer İletişim (Mail/Tel) ve Sosyal Medya Linklerinin Testi
    def test_footer_contact_and_social_links(self):
        self.driver.get(self.base_url)
        actions = ActionChains(self.driver)

        # --- 1. TELEFON LİNKİ ---
        tel_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//footer//a[starts-with(@href, 'tel:')]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tel_link)
        time.sleep(1)
        
        self.show_virtual_cursor(tel_link)
        actions.move_to_element(tel_link).perform()
        time.sleep(0.5)
        assert tel_link.get_attribute("href") == "tel:+8801234567890", "HATA: Telefon linki yanlış veya eksik!"

        # --- 2. E-POSTA LİNKİ ---
        mail_link = self.driver.find_element(By.XPATH, "//footer//a[starts-with(@href, 'mailto:')]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", mail_link)
        time.sleep(0.5)
        
        self.show_virtual_cursor(mail_link)
        actions.move_to_element(mail_link).perform()
        time.sleep(0.5)
        assert mail_link.get_attribute("href") == "mailto:info@insucom.com", "HATA: E-posta linki yanlış!"

        # --- 3. SOSYAL MEDYA LİNKİ ---
        facebook_link = self.driver.find_element(By.XPATH, "//footer//a[contains(@href, 'facebook.com')]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", facebook_link)
        time.sleep(0.5)
        
        self.show_virtual_cursor(facebook_link)
        actions.move_to_element(facebook_link).perform()
        time.sleep(0.5)
        assert facebook_link.get_attribute("target") == "_blank", "HATA: Sosyal medya linkleri yeni sekmede açılmıyor!"
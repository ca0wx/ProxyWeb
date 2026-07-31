# 🌐 ProxyWeb — Canlı Proxy Tara & Otomatik Tarayıcı Başlatıcı

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/ProxyScrape-API_v4-00C7B7?style=for-the-badge&logo=fastapi&logoColor=white" alt="ProxyScrape API" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/OS-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="OS Windows" />
</p>

```
  ___   ___    ___   __  __ __   __   __      __  ___   ___ 
 | _ \ | _ \  / _ \  \ \/ / \ \ / /   \ \    / / | __| | _ )
 |  _/ |   / | (_) |  >  <   \ V /     \ \/\/ /  | _|  | _ \
 |_|   |_|_\  \___/  /_/\_\   |_|       \_/\_/_  |___| |___/

                   By: d'range | Discord: qc2n
```

> **ProxyWeb**, İnternet üzerinden canlı ve çalışan proxy adreslerini anlık olarak çekip doğrulayan, seçilen proxy ile sisteminizde yüklü olan tarayıcıyı tek tıkla gizli/bağımsız proxy modunda otomatik başlatan etkileşimli bir CLI aracıdır.

---

## 🚀 Öne Çıkan Özellikler

- ⚡ **Canlı Proxy Çekme (ProxyScrape API v4):** Dünya genelindeki güncel proxy listelerini anında çeker.
- 🎯 **Esnek Filtreleme Seçenekleri:** 
  - **Protokol:** `HTTP`, `SOCKS4`, `SOCKS5`
  - **Anonimlik Seviyesi:** `Elite`, `Anonymous`, `Transparent`
  - **Timeout Süresi:** `1000 ms`, `2500 ms`, `5000 ms`
- 🩺 **Gerçek Zamanlı Proxy Canlılık Testi (Health Check):** Proxy'leri `https://httpbin.org/ip` üzerinden anlık test eder, yalnızca sorunsuz çalışan canlı proxy'leri önerir.
- 🔍 **Otomatik Sistem Tarayıcısı Tespiti:** Sisteminizde kurulu web tarayıcılarını otomatik tespit eder:
  - 🌐 Google Chrome
  - 🦁 Brave Browser
  - 🌀 Microsoft Edge
  - 🔴 Opera
  - 🦊 Mozilla Firefox
  - 🔲 Chromium
  - 🧭 Safari
- 🚀 **Tek Tıkla Proxy Tarayıcı Başlatma:** Çalışan proxy doğrulandığında, seçtiğiniz tarayıcıyı `--proxy-server` parametresiyle izole şekilde çalıştırır.
- 🎨 **Şık ve Etkileşimli CLI Ara Yüzü:** `InquirerPy` ve `Colorama` altyapısı ile zenginleştirilmiş kullanıcı dostu terminal deneyimi.

---

## 🛠️ Kurulum

### 1. Gereksinimler
Sisteminizde **Python 3.8+** yüklü olmalıdır.

### 2. Depoyu Klonlayın veya İndirin
```bash
git clone https://github.com/kullanici/ProxyWeb.git
cd ProxyWeb
```

### 3. Bağımlılıkları Yükleyin
Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:
```bash
pip install -r requirements.txt
```

---

## 💻 Kullanım

Uygulamayı başlatmak için terminalden `main.py` dosyasını çalıştırmanız yeterlidir:

```bash
python main.py
```

### 🔄 Adım Adım İşleyiş

1. **Protokol Seçin:** `http`, `socks4` veya `socks5` arasından birini seçin.
2. **Anonimlik Derecesi Seçin:** `elite` (Tam gizlilik), `anonymous` veya `transparent`.
3. **Timeout Seçin:** Proxy yanıt süresi sınırı (`1000 ms`, `2500 ms`, `5000 ms`).
4. **Otomatik Test:** Sistem proxy'leri sırayla dener:
   - ❌ Ölü proxy'ler kırmızı uyarı ile atlanır.
   - ✅ Canlı proxy bulunduğunda yeşil onay mesajı görüntülenir.
5. **Tarayıcı Seçimi ve Başlatma:** Onay verdiğinizde sistemdeki hangi tarayıcı ile bağlanmak istediğinizi seçersiniz ve tarayıcınız seçilen proxy üzerinden otomatik açılır!

---

## 📐 Proje Mimarisi & Dosya Yapısı

```
ProxyWeb/
│
├── main.py           # Uygulamanın giriş noktası (Entry Point)
├── selects.py        # İnteraktif CLI menü ve filtre seçim sistemi
├── proxylist.py      # API'den proxy çekme, canlılık kontrolü ve tarayıcı tetikleme
├── browsercheck.py   # Windows sistem tarayıcı yollarını tespit eden modül
└── requirements.txt  # Proje bağımlılıkları (InquirerPy, colorama, requests)
```

| Dosya | Açıklama |
| :--- | :--- |
| [`main.py`](file:///c:/Users/mehme/Desktop/Edit%20Code/ProxyWeb/main.py) | Uygulamayı başlatan ana Python betiği. |
| [`selects.py`](file:///c:/Users/mehme/Desktop/Edit%20Code/ProxyWeb/selects.py) | Kullanıcıdan protokol, anonimlik ve zaman aşımı seçimlerini `InquirerPy` ile alır. |
| [`proxylist.py`](file:///c:/Users/mehme/Desktop/Edit%20Code/ProxyWeb/proxylist.py) | Proxyscrape API'den verileri çeker, `httpbin` ile doğrular ve tarayıcıyı başlatır. |
| [`browsercheck.py`](file:///c:/Users/mehme/Desktop/Edit%20Code/ProxyWeb/browsercheck.py) | Sistemdeki 7 popüler tarayıcının `.exe` yollarını tarayıp tespit eder. |
| [`requirements.txt`](file:///c:/Users/mehme/Desktop/Edit%20Code/ProxyWeb/requirements.txt) | Proje için gerekli Python kütüphaneleri. |

---

## 🌐 Desteklenen Tarayıcılar

| Tarayıcı | Destek Durumu | Otomatik Algılama |
| :--- | :---: | :---: |
| **Google Chrome** | ✅ | ✅ |
| **Brave Browser** | ✅ | ✅ |
| **Microsoft Edge** | ✅ | ✅ |
| **Opera** | ✅ | ✅ |
| **Mozilla Firefox** | ✅ | ✅ |
| **Chromium** | ✅ | ✅ |
| **Safari (Windows)** | ✅ | ✅ |

---

## 🤝 İletişim & Yapımcı

- **Geliştirici:** `d'range`
- **Discord:** `qc2n`

---

## ⚠️ Yasal Uyarı

Bu araç yalnızca eğitim, test ve kişisel gizlilik araştırmaları amacıyla geliştirilmiştir. Kullanıcıların bu aracı kullanırken tabi oldukları yerel yasalara uymaları kendi sorumluluklarındadır.

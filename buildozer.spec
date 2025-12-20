[app]

# (1) Uygulama Ayarları
title = Kkkk App For LO
package.name = lo.ardapapa3.kkkk
package.domain = org.ardapapa3
source.dir = .
source.exclude_dirs = bin, build, venv

# Uygulamanın ana Python dosyası
main.py = insta.py

# Uygulamanın versiyonu. Her yeni APK yapımında bu sayıyı artırman iyi olur!
version = 0.1

# (2) GEREKLİ KÜTÜPHANELER
# insta.py dosyası requests ve os kütüphanelerini kullanıyor.
# Kivy, Buildozer'ın varsayılanı.
requirements = python3, kivy, requests

# (3) Android Ayarları ve İzinler (ÇOK KRİTİK!)

# Uygulamanın kullandığı Android API seviyesi
android.api = 33

# Uygulamanın İnternet ve Harici Depolama İzinleri
# Senin kodun hem Telegram'a bağlanıyor hem de telefonun depolama alanını arıyor,
# bu yüzden bu izinler MUTLAKA açık olmalı.
# NOT: Bu izinler, Android 10+ (API 29+) cihazlarda dosya erişimi için zorunludur.
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (4) Uygulama Görünümü
# Eğer kendi ikonunu eklemek istersen, burayı düzenle:
# icon.filename = %(source.dir)s/icon.png
# orientation = portrait

# (5) Buildozer'ın Varsayılan Diğer Ayarları (Dokunma)
# (Bu kısım, diğer standart ayarları içerir)
# ... (Geri kalan Buildozer varsayılan ayarları) ...

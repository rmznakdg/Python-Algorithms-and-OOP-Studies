import random
import string
import os

class SifreOlusturucu:
    """Rastgele şifre oluşturma işlemlerini ve dosya yönetimini sağlayan sınıf."""
    
    def __init__(self, dosya_yolu="Sifreler.txt"):
        self.dosya_yolu = dosya_yolu

    def sifre_uret(self, adet, uzunluk, kucuk_harf, buyuk_harf, rakam, ozel_karakter, turkce_karakter):
        karakter_havuzu = ""
        if kucuk_harf:
            karakter_havuzu += string.ascii_lowercase
        if buyuk_harf:
            karakter_havuzu += string.ascii_uppercase
        if rakam:
            karakter_havuzu += string.digits
        if ozel_karakter:
            karakter_havuzu += string.punctuation
        if turkce_karakter:
            karakter_havuzu += "çğğıöşüÇĞİÖŞÜ"
            
        if not karakter_havuzu:
            return None
        
        uretilen_sifreler = []
        for _ in range(adet):
            sifre = ''.join(random.choices(karakter_havuzu, k=uzunluk))
            uretilen_sifreler.append(sifre)
            
        return uretilen_sifreler

    def sifreleri_kaydet(self, sifreler, uzunluk):
        with open(self.dosya_yolu, 'a', encoding='utf-8') as file:
            for pwd in sifreler:
                file.write(f"{uzunluk} haneli şifre: {pwd}\n")

    def kayitli_sifreleri_getir(self):
        if os.path.exists(self.dosya_yolu):
            with open(self.dosya_yolu, 'r', encoding='utf-8') as f:
                return f.read()
        return None

    def tum_sifreleri_sil(self):
        if os.path.exists(self.dosya_yolu):
            try:
                os.remove(self.dosya_yolu)
                return True
            except Exception:
                return False
        return False

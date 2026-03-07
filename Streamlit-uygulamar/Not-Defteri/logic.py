from datetime import datetime
import os

class GunlukLogic:
    def __init__(self, dosya_adi="Günlük Programı.txt"):
        self.dosya_adi = dosya_adi

    def notu_kaydet(self, metin):
        """
        Kullanıcının yazdığı metni tarih damgasıyla birlikte dosyaya kaydeder.
        """
        zaman = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(self.dosya_adi, "a", encoding="utf-8") as file:
            file.write(f"[{zaman}]: {metin}\n\n")

    def notlari_oku(self):
        """
        Dosyadaki tüm notları okur ve bir liste olarak döndürür.
        """
        if not os.path.exists(self.dosya_adi):
            return []

        not_listesi = []
        with open(self.dosya_adi, "r", encoding="utf-8") as file:
            icerik = file.read()
            notlar = icerik.strip().split("\n\n") 
            for n in notlar:
                if n.strip():
                    not_listesi.append(n.strip())
                    
        return not_listesi

    def gunlugu_temizle(self):
        """
        Tüm günlüğü sıfırlar (dosyayı boşaltır)
        """
        with open(self.dosya_adi, "w", encoding="utf-8") as file:
            file.write("") # Boş bir string yazarak içeriği sileriz

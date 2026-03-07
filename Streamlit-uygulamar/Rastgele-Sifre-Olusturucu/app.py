import streamlit as st
import os
from logic import SifreOlusturucu

# Sayfa ayarları
st.set_page_config(page_title="Rastgele Şifre Oluşturucu", page_icon="🔐")

st.title("🔐 Rastgele Şifre Oluşturucu")
st.markdown("Bu uygulama ile dilediğiniz özelliklerde **güvenli ve rastgele** şifreler oluşturabilirsiniz.")

# Sınıf örneğini oluştur, dosya yolunu belirle
DOSYA_YOLU = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sifreler.txt')
sifre_motoru = SifreOlusturucu(dosya_yolu=DOSYA_YOLU)

# Yan menü (Ayarlar)
st.sidebar.header("⚙️ Şifre Ayarları")
adet = st.sidebar.number_input("Kaç adet şifre oluşturulsun?", min_value=1, max_value=100, value=1)
uzunluk = st.sidebar.slider("Şifre Uzunluğu", min_value=4, max_value=100, value=12)

st.sidebar.subheader("🔠 Karakter Seçenekleri")
kucuk_harf = st.sidebar.checkbox("Küçük Harfler (a-z)", value=True)
buyuk_harf = st.sidebar.checkbox("Büyük Harfler (A-Z)", value=True)
rakam = st.sidebar.checkbox("Rakamlar (0-9)", value=True)
ozel_karakter = st.sidebar.checkbox("Özel Karakterler (!@#$% vb.)", value=True)
turkce_karakter = st.sidebar.checkbox("Türkçe Karakterler (ç,ğ,ı,ö,ş,ü)", value=False)

if st.button("🚀 Şifre Üret", use_container_width=True):
    sifreler = sifre_motoru.sifre_uret(
        adet, uzunluk, kucuk_harf, buyuk_harf, rakam, ozel_karakter, turkce_karakter
    )
    
    if sifreler:
        st.success(f"{adet} adet şifre başarıyla oluşturuldu!")
        
        # Dosyaya sınıf üzerinden kümülatif olarak kaydet
        sifre_motoru.sifreleri_kaydet(sifreler, uzunluk)
        
        # Ekranda göster
        for pwd in sifreler:
            st.code(pwd, language="")
    else:
        st.error("Lütfen en az bir karakter türü seçiniz!")
        
st.divider()

# Kümülatif olarak kaydedilen şifreleri gösterme bölümü
st.subheader("💾 Kaydedilen Tüm Şifreler (Kümülatif)")
st.markdown("Bugüne kadar üretilip dosyaya kaydedilen tüm şifreler aşağıdadır:")

kayitli_sifreler = sifre_motoru.kayitli_sifreleri_getir()

if kayitli_sifreler:
    st.text_area("Sifreler.txt İçeriği:", value=kayitli_sifreler, height=250, disabled=True)
    
    # 2 sütun oluştur: Biri indirme, diğeri silme butonu için
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.download_button(
            label="📄 Şifreleri İndir",
            data=kayitli_sifreler,
            file_name="Sifreler.txt",
            mime="text/plain",
            use_container_width=True
        )
        
    with col2:
        if st.button("🗑️ Tüm Şifreleri Sil", type="primary", use_container_width=True):
            if sifre_motoru.tum_sifreleri_sil():
                st.success("Tüm şifreler başarıyla silindi!")
                st.rerun()
            else:
                st.error("Şifreler silinirken bir hata oluştu veya dosya bulunamadı.")
else:
    st.info("Henüz kaydedilmiş bir şifre bulunmuyor.")

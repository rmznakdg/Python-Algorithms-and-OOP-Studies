import streamlit as st
from logic import GunlukLogic

gunluk = GunlukLogic()

# Streamlit Sayfa Ayarları
st.set_page_config(
    page_title="Dijital Günlük",
    page_icon="📓",
    layout="centered"
)


# ---------------------------------------------------------
# STREAMLIT ARAYÜZ (GÖRSEL KISIM) 
# ---------------------------------------------------------

st.title("📓 Benim Dijital Günlüğüm")
st.markdown("*Günden güne düşüncelerinizi, aldığınız notları veya öğrendiklerinizi kaydedin.*")
st.divider()

# --- 1. YENİ NOT EKLEME EKRANI ---
st.subheader("Kalemi Eline Al ✍️")

# Oturum durumunu (st.session_state) kullanarak, not kaydedildikten sonra metin kutusunu temizleyeceğiz
if "yeni_not" not in st.session_state:
    st.session_state.yeni_not = ""

# st.text_area: Çok satırlı geniş bir metin girme kutusu
yazilan_metin = st.text_area(
    "Bugün ne yazmak istiyorsunuz?", 
    value=st.session_state.yeni_not,
    height=150,
    placeholder="Düşüncelerinizi buraya yazın..."
)

# "Kaydet" butonu
if st.button("Günlüğe Kaydet", type="primary", use_container_width=True):
    if yazilan_metin.strip() != "":
        # Fonksiyonu çağırıp dosyaya yazdır
        gunluk.notu_kaydet(yazilan_metin)
        
        # Ekranda başarılı mesajı göster
        st.success("Notunuz başarıyla kaydedildi!")
        
        # Metin kutusunu temizleyip sayfayı yenilemek için session_state kullanalım
        st.session_state.yeni_not = ""
        st.rerun()
    else:
        st.warning("Kaydetmek için önce bir şeyler yazmalısınız!")

st.divider()

# --- 2. GEÇMİŞ NOTLARI OKUMA EKRANI ---
st.subheader("Geçmiş Sayfalar 📖")

# Dosyadan notları okuyup liste halinde 'gecmis_notlar' değişkenine atalım
gecmis_notlar = gunluk.notlari_oku()

if not gecmis_notlar:
    st.info("Günlüğünüz henüz boş. Yukarıdan ilk notunuzu ekleyebilirsiniz!")
else:
    # Notları sondan başa (en yeni not en üstte) görünecek şekilde ters çevirelim
    gecmis_notlar.reverse()
    
    # Her bir notu sırayla göstermek için döngü (Orijinal projenizdeki "oku" satırı vizyonu)
    for not_metni in gecmis_notlar:
        # Metni tarih ("[{zaman}]: ") ve gövde ("{metin}") olarak ikiye ayırmaya çalışalım
        if "]: " in not_metni:
            tarih_kismi, metin_kismi = not_metni.split("]: ", 1)
            tarih_kismi = tarih_kismi + "]" # ']' işaretini geri ekle
            
            # Streamlit Expander (Açılır kutu) kullanarak şık bir görünüm elde edelim
            with st.expander(f"📌 {tarih_kismi}"):
                st.write(metin_kismi)
        else:
            # Beklenmedik bir format geldiyse olduğu gibi yazdır
            st.code(not_metni)

st.divider()

# Yan menü veya alt kısımda ekstra seçenekler koyabiliriz
with st.sidebar:
    st.header("⚙️ Ayarlar")
    st.write(f"📂 **Kayıt Dosyası:** `{gunluk.dosya_adi}`")
    st.write(f"📝 **Toplam Not Sayısı:** `{len(gecmis_notlar)}`")
    
    st.markdown("---")
    
    # Tüm notları silmek için tehlikeli (kırmızımsı) buton kurgusu
    st.error("⚠️ Tehlikeli Bölge")
    if st.button("Tüm Günlüğü Sil"):
        gunluk.gunlugu_temizle()
        st.success("Günlük tamamen temizlendi.")
        st.rerun()

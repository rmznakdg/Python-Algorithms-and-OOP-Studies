import streamlit as st
from logic import Scorboard

# Streamlit Sayfa Ayarları (Tarayıcı sekmesindeki başlık ve simge)
st.set_page_config(
    page_title="Masa Tenisi Skorbord", 
    page_icon="🏓", 
    layout="centered"
)

# Oyunu başlatan veya sıfırlayan yardımcı fonksiyon
def reset_oyun(p1, p2):
    # NESNEYİ "st.session_state" İÇİNDE SAKLIYORUZ!
    # Bu, Streamlit'teki en önemli yapıdır. Butonlara her tıklandığında Python dosyası 
    # baştan aşağı tekrar çalışır. Verilerin kaybolmaması için session_state kullanılır.
    st.session_state.oyun = Scorboard(p1, p2)

# ==========================================
# STREAMLIT ARAYÜZ (GÖRSEL KISIM) 
# ==========================================

st.title("🏓 Masa Tenisi Skorbord")
st.markdown("*Python ve Streamlit kütüphanesi ile geliştirilmiş interaktif skor takibi.*")

# 1. SOL MENÜ (Sidebar) - Oyun ayarları için
with st.sidebar:
    st.header("⚙️ Oyun Ayarları")
    p1_input = st.text_input("1. Oyuncu Adı", value="Oyuncu 1")
    p2_input = st.text_input("2. Oyuncu Adı", value="Oyuncu 2")
    
    # "Yeni Oyun Başlat" butonuna tıklanırsa...
    if st.button("Yeni Oyun Başlat", type="primary", use_container_width=True):
        reset_oyun(p1_input, p2_input)

# Eğer sayfa ilk defa açıldıysa 'oyun' state'i henüz yoktur, oluşturalım:
if 'oyun' not in st.session_state:
    reset_oyun(p1_input, p2_input)

# Kodun kalanında bu değişkene oyun diyelim (Daha kolay yazmak için)
oyun = st.session_state.oyun

# 2. MESAJ ALANI VE BALON EFEKTİ (Streamlit'in güzel taraflarından)
if oyun.mesaj:
    if "kazandı" in oyun.mesaj:
        st.success(oyun.mesaj)
        st.balloons() # Uygulama ekranında kutlama balonları uçurur
    else:
        st.info(oyun.mesaj)

# 3. KURA ÇEKME VE SERVİS SIRASI GÖSTERGESİ
st.subheader("Hakem Masası")
col_bilgi, col_buton = st.columns([2, 1])

with col_bilgi:
    servis = oyun.servis_kimde()
    # Metni Markdown tarzında yazdırabiliriz
    st.write(f"**📣 Servis Sırası:** `{servis}`")

with col_buton:
    # disabled (pasif bırakma) mantığı çok basittir, Kura çekildiyse veya oyun bittiyse butonu kilitle
    if st.button("🎲 Kura Çek", use_container_width=True, disabled=(oyun.ilk_baslayan is not None) or oyun.oyun_bitti):
        oyun.kim_baslayacak()
        st.rerun() # Sayfayı günceller ve kod baştan okunur (ama session_state'deki veriler korunur!)

st.divider()

# 4. SKORBORD EKRANI (İki Sütunlu Yapı)
st.subheader("Skor Tablosu")
col1, col2 = st.columns(2)

# Birinci Oyuncunun Sütunu
with col1:
    # Görselliği biraz zenginleştirmek için HTML takıları (st.markdown) ile özelleştirme yapabiliriz
    st.markdown(f"<h3 style='text-align: center; color: #60a5fa;'>{oyun.player1}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{oyun.score1}</h1>", unsafe_allow_html=True)
    
    # Sayı Alma butonu
    if st.button(f"+1 Sayı Al ({oyun.player1})", use_container_width=True, disabled=oyun.oyun_bitti or (oyun.ilk_baslayan is None)):
        oyun.score_player1()
        st.rerun()

# İkinci Oyuncunun Sütunu
with col2:
    st.markdown(f"<h3 style='text-align: center; color: #f43f5e;'>{oyun.player2}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{oyun.score2}</h1>", unsafe_allow_html=True)
    
    if st.button(f"+1 Sayı Al ({oyun.player2})", use_container_width=True, disabled=oyun.oyun_bitti or (oyun.ilk_baslayan is None)):
        oyun.score_player2()
        st.rerun()

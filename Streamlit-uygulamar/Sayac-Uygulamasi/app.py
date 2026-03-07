import streamlit as st
import time
from logic import Counter

# Sayfa ayarları
st.set_page_config(page_title="Sayaç ve Zamanlayıcı Projesi", page_icon="⏱️", layout="centered")

# Session state'te Counter sınıfının başlatılması
if 'counter' not in st.session_state:
    st.session_state.counter = Counter()

counter = st.session_state.counter

st.title("⏱️ Sayaç ve Zamanlayıcı Uygulaması")
st.markdown("Bu uygulama üzerinden **manuel sayaç** ve **zamanlayıcı (kronometre)** sistemini bir arada kullanabilirsiniz.")

st.divider()

# --- ZAMANLAYICI (KRONOMETRE) BÖLÜMÜ ---
st.header("⏳ Zamanlayıcı (Kronometre)")

# Süreyi Gösteren Konteyner
st.markdown(f"<h1 style='text-align: center; font-size: 80px; color: #4CAF50;'>{counter.get_time_formatted()}</h1>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("▶️ Başlat / Devam", use_container_width=True):
        counter.start_timer()
        st.rerun()

with col2:
    if st.button("⏸️ Durdur (Pause)", use_container_width=True):
        counter.pause_timer()
        st.rerun()

with col3:
    if st.button("🚩 Tur (Lap)", use_container_width=True):
        counter.record_lap()
        st.rerun()

with col4:
    if st.button("🔄 Sıfırla", key="reset_sw", use_container_width=True):
        counter.reset_stopwatch()
        st.rerun()

# Turları Görüntüleme
if counter.laps:
    st.write("### 🏁 Kaydedilmiş Turlar")
    for i, lap in enumerate(counter.laps):
        # Turları daha düzenli bir formatta yazdır
        st.info(f"**Tur {i + 1}:** {lap}")

st.divider()

# --- MANUEL SAYAÇ BÖLÜMÜ ---
st.header("🔢 Manuel Sayaç")

st.markdown(f"<h2 style='text-align: center;'>Mevcut Değer: <span style='color: #2196F3;'>{counter.count}</span></h2>", unsafe_allow_html=True)

m_col1, m_col2, m_col3 = st.columns(3)

with m_col1:
    inc_val = st.number_input("Artırma Miktarı", min_value=1, value=1, step=1, key="inc")
    if st.button("➕ Artır", use_container_width=True):
        counter.increment_counter(inc_val)
        st.rerun()

with m_col2:
    dec_val = st.number_input("Azaltma Miktarı", min_value=1, value=1, step=1, key="dec")
    if st.button("➖ Azalt", use_container_width=True):
        counter.decrement_counter(dec_val)
        st.rerun()

with m_col3:
    start_val = st.number_input("Başlangıç Değeri", value=0, step=1, key="start_val")
    if st.button("⚙️ Ayarla", use_container_width=True):
        counter.starting_value(start_val)
        st.rerun()

# Otomatik yenileme döngüsü: Eğer kronometre aktifse, saniyenin onda biri sürede ekranı düzenli yeniler.
# Bu sayede kronometre süresinin aktığı ekrana anlık yansır.
if counter.is_running:
    time.sleep(0.1)
    st.rerun()

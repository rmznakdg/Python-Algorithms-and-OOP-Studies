import streamlit as st
from logic import TodoLogic

# Sayfa ayarları
st.set_page_config(page_title="To-Do List Programı", page_icon="📝", layout="centered")

# Session state başlatma
if 'todo_logic' not in st.session_state:
    st.session_state.todo_logic = TodoLogic()

logic = st.session_state.todo_logic

st.title("📝 To-Do List Programı")
st.divider() # use st.divider() instead of st.markdown("---")

# Görev Ekleme Bölümü
st.subheader("Yeni Görev Ekle")
with st.form(key='add_task_form', clear_on_submit=True):
    col_input, col_btn = st.columns([4, 1])
    with col_input:
        yeni_gorev = st.text_input("Eklemek istediğiniz görev:", label_visibility="collapsed", placeholder="Görev girin...")
    with col_btn:
        submit_button = st.form_submit_button(label='Ekle', use_container_width=True)
        
    if submit_button and yeni_gorev.strip():
        logic.gorev_ekle(yeni_gorev.strip())
        st.success(f"'{yeni_gorev}' listeye eklendi!")
        st.rerun()

# Görevleri Listeleme ve İşlemler
st.divider()
st.subheader("📌 Yapılacak Görevler")
todos = logic.get_todos()

if not todos:
    st.info("Listede henüz bir görev yok. Yukarıdan görev ekleyebilirsiniz.")
else:
    for i, gorev in enumerate(todos):
        col1, col2, col3 = st.columns([6, 1, 1])
        with col1:
            # We can use st.markdown with standard markdown formatting
            st.markdown(f"**{i+1}.** {gorev}")
        with col2:
            if st.button("✔️", key=f"tamamla_{i}", help="Görevi Tamamla", use_container_width=True):
                logic.gorevi_tamamla(i)
                st.rerun()
        with col3:
            if st.button("🗑️", key=f"sil_{i}", help="Görevi Sil", use_container_width=True):
                logic.gorev_sil(i)
                st.rerun()

# Tamamlanan Görevler
st.divider()
st.subheader("✅ Tamamlanan Görevler")
completed = logic.get_completed()

if not completed:
    st.info("Henüz tamamlanan görev yok.")
else:
    for i, gorev in enumerate(completed):
        st.markdown(f"- ~~{gorev}~~")

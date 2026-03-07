import streamlit as st
from logic import Student

# Sayfa ayarları
st.set_page_config(page_title="Öğrenci Yönetim Sistemi", page_icon="🎓", layout="wide")

st.title("🎓 Öğrenci Yönetim Sistemi")
st.markdown("Öğrenci bilgilerini girin, not ekleyin ve öğrencileri karşılaştırın.")

# Session state initialization for students
if 'students' not in st.session_state:
    st.session_state['students'] = {}

# Sidebar for navigation
st.sidebar.title("Menü")
menu = ["Öğrenci Ekle", "Not Ekle", "Öğrenci Sorgula / Listele", "Öğrencileri Karşılaştır"]
choice = st.sidebar.radio("İşlem Seçin", menu)

if choice == "Öğrenci Ekle":
    st.header("Yeni Öğrenci Ekle")
    name = st.text_input("Öğrenci Adı")
    grades_input = st.text_input("Başlangıç Notları (Virgülle ayırarak girin, örn: 80, 90)")
    
    if st.button("Öğrenciyi Kaydet"):
        if name:
            if name in st.session_state['students']:
                st.warning("Bu isimde bir öğrenci zaten mevcut!")
            else:
                try:
                    grades = []
                    if grades_input.strip():
                        grades = [int(g.strip()) for g in grades_input.split(",")]
                    
                    student = Student(name, grades)
                    st.session_state['students'][name] = student
                    st.success(f"✅ Öğrenci '{name}' başarıyla eklendi!")
                except ValueError:
                    st.error("❌ Lütfen notları geçerli bir formatta girin (sadece tam sayı).")
        else:
            st.error("❌ Lütfen öğrenci adını girin.")

elif choice == "Not Ekle":
    st.header("Öğrenciye Not Ekle")
    if not st.session_state['students']:
        st.info("Sistemde henüz öğrenci bulunmuyor. Lütfen önce öğrenci ekleyin.")
    else:
        student_name = st.selectbox("Öğrenci Seçin", list(st.session_state['students'].keys()))
        new_grades = st.text_input("Eklenecek Notlar (Virgülle ayırarak girin, örn: 75, 85)")
        
        if st.button("Notları Kaydet"):
            if new_grades.strip():
                try:
                    grades_to_add = [int(g.strip()) for g in new_grades.split(",")]
                    student = st.session_state['students'][student_name]
                    student.add_grade(grades_to_add)
                    st.success(f"✅ '{student_name}' adlı öğrenciye notlar başarıyla eklendi!")
                except ValueError as e:
                    st.error(f"❌ Hata: {e}")
            else:
                st.error("❌ Lütfen eklenecek notları girin.")

elif choice == "Öğrenci Sorgula / Listele":
    st.header("Öğrenci Listesi ve Sorgulama")
    
    if not st.session_state['students']:
        st.info("Sistemde henüz öğrenci bulunmuyor.")
    else:
        search_query = st.text_input("🔍 Öğrenci Ara (Adının bir kısmını yazabilirsiniz)")
        
        # Passing threshold
        threshold = st.number_input("Geçme Notu Barajı", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
        
        st.subheader("Öğrenci Bilgileri")
        found = False
        for name, student in st.session_state['students'].items():
            if search_query.lower() in name.lower():
                found = True
                avg = student.average()
                is_pass = student.is_passing(threshold)
                status = "Geçti" if is_pass else "Kaldı"
                color = "green" if is_pass else "red"
                
                with st.expander(f"{name} | Ortalama: {avg:.2f} | Durum: {status}"):
                    st.write(f"**Notlar:** {', '.join(map(str, student.grades)) if student.grades else 'Kayıtlı not yok'}")
                    st.write(f"**Ortalama:** {avg:.2f}")
                    st.markdown(f"**Durum:** :{color}[{status}] (Baraj: {threshold})")
        if not found:
            st.warning("Arama kriterinize uygun öğrenci bulunamadı.")

elif choice == "Öğrencileri Karşılaştır":
    st.header("Öğrenci Karşılaştırma")
    if len(st.session_state['students']) < 2:
        st.info("Karşılaştırma yapmak için en az 2 öğrenci sistemde kayıtlı olmalıdır.")
    else:
        student_list = list(st.session_state['students'].keys())
        st.write("Karşılaştırmak istediğiniz öğrencileri seçin:")
        
        col1, col2 = st.columns(2)
        with col1:
            student1_name = st.selectbox("1. Öğrenci", student_list, index=0)
        with col2:
            student2_name = st.selectbox("2. Öğrenci", student_list, index=1 if len(student_list) > 1 else 0)
            
        if st.button("Karşılaştır"):
            if student1_name == student2_name:
                st.warning("Lütfen iki farklı öğrenci seçin.")
            else:
                s1 = st.session_state['students'][student1_name]
                s2 = st.session_state['students'][student2_name]
                
                s1_avg = s1.average()
                s2_avg = s2.average()
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label=f"{student1_name} Ortalaması", value=f"{s1_avg:.2f}")
                    st.write(f"**Notlar:** {', '.join(map(str, s1.grades)) if s1.grades else 'Yok'}")
                with col2:
                    st.metric(label=f"{student2_name} Ortalaması", value=f"{s2_avg:.2f}", delta=f"{(s2_avg - s1_avg):.2f}" if s1_avg != s2_avg else "0.00")
                    st.write(f"**Notlar:** {', '.join(map(str, s2.grades)) if s2.grades else 'Yok'}")
                    
                st.subheader("Sonuç")
                if s1_avg > s2_avg:
                    st.success(f"🏆 **{student1_name}**, {student2_name}'den daha yüksek ortalamaya sahip.")
                elif s2_avg > s1_avg:
                    st.success(f"🏆 **{student2_name}**, {student1_name}'den daha yüksek ortalamaya sahip.")
                else:
                    st.info("🔹 Her iki öğrenci de aynı ortalamaya sahip.")

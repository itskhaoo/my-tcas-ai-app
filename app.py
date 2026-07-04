import streamlit as st
import pandas as pd

# --- 1. ตั้งค่าหน้าเว็บให้ดูโปรระดับ TikTok (Page Config) ---
st.set_page_config(
    page_title="TCAS AI Solution | แพลนเนอร์อัจฉริยะ",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. โค้ดตกแต่ง CSS ขั้นสูง (Modern UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Itim&family=Kanit:wght@300;400;600&display=swap');

    /* ใช้ฟอนต์ Itim สำหรับความน่ารัก และ Kanit สำหรับข้อมูลที่อ่านง่าย */
    html, body, [class*="css"] {
        font-family: 'Itim', cursive;
    }

    /* พื้นหลังโทนสว่างดูสะอาดตา */
    .stApp {
        background-color: #F8F9FA;
    }

    /* ตกแต่ง Sidebar ให้ดูทันสมัย */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFEDF0 0%, #FFFFFF 100%);
        border-right: 1px solid #FFE4E6;
    }

    /* การ์ดแสดงผล (Glassmorphism Light) */
    .result-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #FFF1F2;
        transition: 0.3s;
        text-align: center;
        margin-bottom: 20px;
    }
    .result-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(255, 183, 178, 0.3);
    }

    /* ปุ่มกดสไตล์มนโค้งน่ารัก */
    .stButton>button {
        width: 100%;
        border-radius: 30px !important;
        background: linear-gradient(90deg, #FFB7B2 0%, #FF8B94 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 12px 0 !important;
        box-shadow: 0 4px 10px rgba(255, 139, 148, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ส่วนของเมนู Sidebar ---
with st.sidebar:
    st.image("https://www.mytcas.com/assets/img/logo-mytcas.png", width=120)
    st.markdown("### ✨ เมนูหลัก")
    page = st.radio("ไปที่หน้า:", [
        "🏠 หน้าหลัก (Home)",
        "📚 ศูนย์ความรู้ TCAS",
        "💬 AI Chat ถาม-ตอบ",
        "🎯 วางแผน Admission"
    ])
    st.divider()
    st.success("🤖 AI พร้อมช่วยเหลือคุณแล้ว")

# --- 4. การจัดการเนื้อหาแต่ละหน้า ---

if page == "🏠 หน้าหลัก (Home)":
    st.title("🚀 ยินดีต้อนรับสู่ TCAS AI Solution")
    st.markdown("### อัปเดตข่าวสารล่าสุด ✨")
    c1, c2 = st.columns(2)
    with c1:
        st.info("📌 **ประกาศ:** เปิดระบบลงทะเบียน myTCAS วันแรกแล้วนะ!")
    with c2:
        st.warning("📅 **Deadline:** รอบ Portfolio กำลังจะหมดเขตใน 5 วัน")

elif page == "📚 ศูนย์ความรู้ TCAS":
    st.title("📚 คลังความรู้เด็ก 68-69")
    tab1, tab2 = st.tabs(["ระบบ TCAS", "ตารางสอบ"])
    with tab1:
        st.write("สรุป 4 รอบการรับสมัครแบบเข้าใจง่าย...")
    with tab2:
        st.write("รวมวันสอบ TGAT/TPAT และ A-Level...")

elif page == "💬 AI Chat ถาม-ตอบ":
    st.title("💬 ถามพี่ AI ได้เลย!")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("อยากรู้อะไรเกี่ยวกับ TCAS ถามมาเลย..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            response = f"พี่ AI กำลังวิเคราะห์เรื่อง '{prompt}' ให้รอสักครู่นะคะ ✨"
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

elif page == "🎯 วางแผน Admission":
    st.title("🎯 วางแผนกลยุทธ์สอบติด")
    st.markdown("#### กรอกข้อมูลเพื่อวิเคราะห์โอกาส")
    
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        gpax = st.number_input("เกรดเฉลี่ยสะสม (GPAX)", 0.0, 4.0, 3.5)
    with col_input2:
        faculty = st.text_input("คณะ/สาขาที่เล็งไว้", placeholder="เช่น บัญชี มธ.")

    if st.button("✨ เริ่มวิเคราะห์แผนการเรียน"):
        st.balloons()
        st.markdown("---")
        m1, m2, m3 = st.columns(3)
        
        with m1:
            st.markdown("""<div class="result-card">
                <h2 style='color:#FF6B6B;'>💖 Dream</h2>
                <p><b>เสี่ยงสูง</b></p>
                <p>จุฬาลงกรณ์มหาวิทยาลัย</p>
            </div>""", unsafe_allow_html=True)
            st.progress(30)
            
        with m2:
            st.markdown("""<div class="result-card">
                <h2 style='color:#4D96FF;'>⚖️ Match</h2>
                <p><b>เหมาะสม</b></p>
                <p>มหาวิทยาลัยธรรมศาสตร์</p>
            </div>""", unsafe_allow_html=True)
            st.progress(65)
            
        with m3:
            st.markdown("""<div class="result-card">
                <h2 style='color:#6BCB77;'>✅ Safe</h2>
                <p><b>ปลอดภัย</b></p>
                <p>มหาวิทยาลัยเกษตรศาสตร์</p>
            </div>""", unsafe_allow_html=True)
            st.progress(90)
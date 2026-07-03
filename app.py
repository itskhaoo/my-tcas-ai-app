import streamlit as st
import pandas as pd

# --- การตั้งค่าเริ่มต้น ---
st.set_page_config(page_title="TCAS AI Solution", layout="wide", initial_sidebar_state="expanded")

# --- ส่วนของเมนูหลัก (Sidebar) ตามโครงสร้างที่คุณวางไว้ ---
with st.sidebar:
    st.image("https://www.mytcas.com/assets/img/logo-mytcas.png", width=100)
    st.title("ระบบนำทาง")
    page = st.selectbox("เลือกบริการ:", [
        "1. หน้าแรก (Homepage)",
        "2. ศูนย์ความรู้ TCAS",
        "3. AI ถาม-ตอบ (Real-time)",
        "4. วางแผนการสมัคร (Admission & Strategy)"
    ])
    st.divider()
    st.caption("Powered by AI TCAS Assistant")

# --- 1. หน้าแรก (Homepage) ---
if page == "1. หน้าแรก (Homepage)":
    st.title("🚀 ยินดีต้อนรับสู่ระบบวางแผน TCAS")
    st.subheader("อัปเดตข่าวสารและกำหนดการสำคัญ")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("📌 **ข่าวล่าสุด:** ทปอ. ประกาศปรับเกณฑ์การคัดเลือกรอบ 3")
        st.info("📌 **ข่าวล่าสุด:** เปิดระบบลงทะเบียน myTCAS วันแรก")
    with col2:
        st.warning("📅 **กำหนดการสำคัญ:**\n- 1-15 ก.ค.: รอบ Portfolio\n- 1-10 ส.ค.: ประกาศผลรอบ 1")

# --- 2. ศูนย์ความรู้ TCAS (TCAS Learning Center) ---
elif page == "2. ศูนย์ความรู้ TCAS":
    st.title("📚 TCAS Learning Center")
    with st.expander("ระบบ TCAS คืออะไร?"):
        st.write("อธิบายรายละเอียด 4 รอบการรับสมัคร...")
    with st.expander("เจาะลึก TGAT/TPAT และ A-Level"):
        st.write("สรุปเนื้อหาที่ต้องสอบและค่าน้ำหนักคะแนน...")

# --- 3. AI ถาม-ตอบ (AI Chat Assistant) ---
elif page == "3. AI ถาม-ตอบ (Real-time)":
    st.title("💬 AI Chat Assistant")
    st.write("ถามคำถามเกี่ยวกับเกณฑ์การรับสมัครได้ทันที")
    user_q = st.text_input("พิมพ์คำถามของคุณที่นี่...")
    if st.button("ส่งคำถาม"):
        # ในอนาคตสามารถเชื่อมต่อกับ AI จากแหล่งข้อมูลของคุณได้
        st.chat_message("assistant").write(f"วิเคราะห์คำถาม '{user_q}' จากฐานข้อมูลระเบียบการล่าสุด...")

# --- 4. วางแผนการสมัคร (หัวใจหลักของระบบ) ---
elif page == "4. วางแผนการสมัคร (Admission & Strategy)":
    st.title("🎯 AI Strategy Planner")
    
    # ส่วนกรอกข้อมูล (GPAX & คะแนน)
    st.header("Step 1: กรอกข้อมูลส่วนตัว")
    c1, c2 = st.columns(2)
    with c1:
        gpax = st.number_input("คะแนน GPAX (6 เทอม)", 0.0, 4.0, 3.5)
    with c2:
        target_faculty = st.text_input("คณะที่อยากเข้า (เช่น วิศวกรรมศาสตร์)")

    # ส่วนวิเคราะห์ (AI Admission Guide)
    if st.button("วิเคราะห์โอกาสและวางแผน"):
        st.header("Step 2: ผลการวิเคราะห์ (Personal Roadmap)")
        
        # ส่วนแสดงผล Dream/Match/Safe
        m1, m2, m3 = st.columns(3)
        with m1:
            st.error("🔥 **Dream (เสี่ยงสูง)**")
            st.write("มหาวิทยาลัยอันดับ 1")
            st.progress(30)
        with m2:
            st.warning("⚖️ **Match (เหมาะสม)**")
            st.write("มหาวิทยาลัยอันดับ 2")
            st.progress(65)
        with m3:
            st.success("✅ **Safe (ปลอดภัย)**")
            st.write("มหาวิทยาลัยอันดับ 3")
            st.progress(90)
            
        st.divider()
        st.balloons()
        st.success("🎉 **SUCCESS!** คุณได้แผนการเตรียมตัวเรียบร้อยแล้ว พร้อมสมัคร TCAS!")

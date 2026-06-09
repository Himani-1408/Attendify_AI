import streamlit as st
import os

st.set_page_config(page_title="About - Attendify", page_icon="ℹ️", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #000000, #0a0a0a);
    color: white;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
}

h1, h2, h3 {
    color: #00FFD1;
}

/* Links styling */
a {
    color: #00FFD1;
    text-decoration: none;
    font-weight: bold;
}
a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# ---------------- 1. TITLE ----------------
st.markdown("<h1 style='text-align:center;'>🎓 Attendify</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Smart AI-Based Attendance System</h3>", unsafe_allow_html=True)

st.divider()

# ---------------- 2. PROJECT OVERVIEW ----------------
st.markdown("## 📌 Project Overview")
st.markdown("""
<div class='card'>
Attendify is an AI-powered attendance management system that automates the process 
of marking attendance using real-time Face Recognition technology. The system captures 
faces through a webcam, identifies registered students, and marks attendance automatically 
in a database.

It reduces manual effort, prevents proxy attendance, and improves accuracy by enabling 
fast and reliable multi-face recognition in a single frame.
</div>
""", unsafe_allow_html=True)

# ---------------- 3. OBJECTIVE ----------------
st.markdown("## 🎯 Objective")
st.markdown("""
<div class='card'>
<ul>
<li>Eliminate proxy attendance</li>
<li>Reduce manual workload for faculty</li>
<li>Improve accuracy and efficiency</li>
<li>Enable real-time monitoring</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------------- 4. FEATURES ----------------
st.markdown("## 🚀 Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
    🔍 Face Recognition System <br>
    🎥 Real-time Face Detection <br>
    👥 Multi-Face Recognition <br>
    🧠 AI-based Face Matching  
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    🗄️ Database Integration (SQLite) <br>
    🛑 Duplicate Face Prevention <br>
    ⚡ Automatic Attendance Marking <br>
    📊 Real-time Attendance Tracking  
    </div>
    """, unsafe_allow_html=True)

# ---------------- 5. TECHNOLOGIES ----------------
st.markdown("## 🛠️ Technologies Used")

st.markdown("""
<div class='card'>
<ul>
<li><b>Python</b> – Core programming language for backend logic</li>
<li><b>OpenCV</b> – Real-time webcam capture and image processing</li>
<li><b>Face Recognition Library</b> – Face encoding and matching using deep learning</li>
<li><b>Streamlit</b> – Web-based user interface and application framework</li>
<li><b>SQLite</b> – Database for storing student and attendance records</li>
<li><b>NumPy</b> – Numerical operations and encoding calculations</li>
<li><b>PIL (Pillow)</b> – Image conversion and processing</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------------- 6. DEVELOPER INFO ----------------
st.markdown("## 👩‍💻 Developer Info")

col1, col2 = st.columns(2)

# ----------- YOUR INFO -----------
with col1:
    img_path1 = os.path.join(os.path.dirname(__file__), "../assets/mine photo.jpg")
    st.image(img_path1, use_container_width=True)

    st.markdown("""
    <div class='card'>
    <h3>Himani Chaudhary</h3>
    B.Tech - Artificial Intelligence & Machine Learning <br><br>

    <b>Role: AI & System Development Lead</b> <br><br>

    <ul>
    <li>Designed and implemented the face recognition system</li>
    <li>Developed real-time attendance logic and face matching algorithms</li>
    <li>Integrated AI model with the application for automation</li>
    </ul>

    <br>

    🔗 <a href="https://www.linkedin.com/in/himani-chaudhary-747a77304/" target="_blank">LinkedIn</a> &nbsp;&nbsp;
    💻 <a href="https://github.com/Himani-1408" target="_blank">GitHub</a> &nbsp;&nbsp;
    📧 chimani702@gmail.com
    </div>
    """, unsafe_allow_html=True)

# ----------- FRIEND INFO -----------
with col2:
    img_path2 = os.path.join(os.path.dirname(__file__), "../assets/mine photo1.jpeg")  # 👈 add image
    st.image(img_path2, use_container_width=True)

    st.markdown("""
    <div class='card'>
    <h3>Vanshika Singh</h3>
    B.Tech - Artificial Intelligence & Machine Learning br><br>

    <b>Role: Database & System Integration Lead</b><br><br>

    <ul>
    <li>Designed and managed SQLite database</li>
    <li>Implemented student and attendance data storage</li>
    <li>Handled backend integration with UI</li>
    <li>Performed testing and system optimization</li>
    </ul>

    <br>
    
    🔗 <a href="https://www.linkedin.com/in/vanshika-singh-a38a48282/" target="_blank">LinkedIn</a> &nbsp;&nbsp;
    💻 <a href="https://github.com/kxagi" target="_blank">GitHub</a> &nbsp;&nbsp;
    📧 Vanshika.singhh25@gmail.com
    </div>
    """, unsafe_allow_html=True)

# ---------------- 7. FUTURE SCOPE ----------------
st.markdown("## 🌟 Future Scope")
st.markdown("""
<div class='card'>
<ul>
<li>Cloud database integration for centralized data access</li>
<li>Mobile application support for remote attendance</li>
<li>Advanced face recognition with improved accuracy</li>
<li>Live classroom monitoring using CCTV integration</li>
<li>Role-based authentication system (Admin/Teacher/Student)</li>
<li>Automated report generation (CSV/Excel)</li>
<li>Integration with timetable and academic management system</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("<p style='text-align:center;'>© 2026 Attendify </p>", unsafe_allow_html=True)
import streamlit as st

st.set_page_config(page_title="Help - Attendify", page_icon="❓", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #000000;
    color: white;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    border-left: 5px solid #00FFD1;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>❓ Help & User Guide</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Follow these steps to use Attendify easily</p>", unsafe_allow_html=True)

st.divider()

# ---------------- STEP 1 ----------------
st.markdown("### 🧑‍🎓 Step 1: Student Registration")
st.markdown("""
<div class='card'>
- Go to <b>Student Registration</b> page  
- Enter Name, Roll Number, Department, Course  
- Click <b>Capture Face</b>  
- System will store your face encoding  
</div>
""", unsafe_allow_html=True)

# ---------------- STEP 2 ----------------
st.markdown("### 🎥 Step 2: Start Attendance")
st.markdown("""
<div class='card'>
- Faculty starts a lecture session  
- Open <b>Take Attendance</b> page  
- Webcam will activate automatically  
</div>
""", unsafe_allow_html=True)

# ---------------- STEP 3 ----------------
st.markdown("### 👁️ Step 3: Face Recognition")
st.markdown("""
<div class='card'>
- System detects your face  
- Matches with registered data  
- Shows your name if recognized  
</div>
""", unsafe_allow_html=True)

# ---------------- STEP 4 ----------------
st.markdown("### 🧠 Step 4: Liveness Detection")
st.markdown("""
<div class='card'>
- Perform actions like blinking or smiling  
- Ensures you are physically present  
- Prevents fake attendance using photos  
</div>
""", unsafe_allow_html=True)

# ---------------- STEP 5 ----------------
st.markdown("### ✅ Step 5: Attendance Marking")
st.markdown("""
<div class='card'>
- Once verified, attendance is marked automatically  
- Duplicate attendance is prevented  
</div>
""", unsafe_allow_html=True)

# ---------------- STEP 6 ----------------
st.markdown("### 📊 Step 6: View Dashboard")
st.markdown("""
<div class='card'>
- Go to Dashboard page  
- View attendance records  
- Analyze performance using charts  
</div>
""", unsafe_allow_html=True)

# ---------------- STEP 7 ----------------
st.markdown("### 📧 Step 7: Notifications (Optional)")
st.markdown("""
<div class='card'>
- Students may receive attendance updates  
- Email alerts can be enabled in future  
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------- TIPS ----------------
st.markdown("## 💡 Tips for Best Use")

st.markdown("""
<div class='card'>
- Ensure proper lighting for face detection  
- Look directly at the camera  
- Avoid multiple people in frame  
- Keep camera stable  
</div>
""", unsafe_allow_html=True)
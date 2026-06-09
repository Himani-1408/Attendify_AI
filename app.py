import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Attendify", layout="centered", page_icon="🎓")

# -----------------------------
# Custom CSS for Dark Theme
# -----------------------------
st.markdown(
    """
    <style>
    /* Background */
    .reportview-container {
        background-color: #000000;
        color: white;
    }
    /* Sidebar */
    .sidebar .sidebar-content {
        background-color: #111111;
        color: white;
    }
    /* Buttons */
    div.stButton > button {
        background-color: #000000;
        color: white;
        border: 2px solid white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    div.stButton > button:hover {
        background-color: #222222;
        color: #ffffff;
    }
    /* Headings */
    h1, h2, h3, h4, h5 {
        color: #ffffff;
    }
    /* Links */
    a {
        color: #4B8BBE;
    }
    /* Inputs */
    input, textarea {
        background-color: #222222;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Dummy credentials
USERNAME = "admin"
PASSWORD = "1234"

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# LOGIN PAGE
# -----------------------------
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center;'>🔐 Admin Login</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:16px;'>Welcome! Please login to access your university dashboard.</p>", unsafe_allow_html=True)

    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Invalid credentials. Try again.")

# -----------------------------
# AFTER LOGIN
# -----------------------------
else:
    st.sidebar.success("Logged in as Admin")

    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # Landing / Dashboard
    st.markdown("<h1 style='text-align: center;'>🎓 Welcome to Admin Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:16px;'>Your smart, real-time attendance management system.</p>", unsafe_allow_html=True)

    # Navigation Cards
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📝 Student Registration")
        st.write("Register new students with face encoding for real-time attendance tracking.")
        if st.button("Go to Registration"):
            st.switch_page("pages/1_Student_Registration.py")

    with col2:
        st.markdown("### 🎥 Attendance System")
        st.write("Mark attendance automatically using face recognition and liveness detection.")
        if st.button("Go to Attendance"):
            st.switch_page("pages/2_Attendance.py")

    st.markdown("---")
    st.markdown("💡 Use the sidebar to logout or navigate additional pages like Dashboard, About, Contact, Help.")
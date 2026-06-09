import streamlit as st

st.set_page_config(page_title="Contact - Attendify", page_icon="📞", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, Black, Black);
    color: white;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>📞 Contact Us</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>If you have any questions, feedback, or suggestions regarding <span style='font-weight:bold; color:red'>ATTENDIFY</span>, feel free to reach out.</p>", unsafe_allow_html=True)

st.divider()

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1,2])

# -------- LEFT: INFO --------
with col1:
    st.markdown("""
    <div class='card'>
    <h3>📍 Get in Touch</h3>
    📧 Email: <a href="mailto:attendify02@gmail.com">attendify02@gmail.com</a> <br><br>
    📱 Phone: +91 827399****  <br><br>
    📍 Location: India <br><br>
    
    💬 We are always happy to help and improve the system based on your feedback.
    </div>
    """, unsafe_allow_html=True)

# -------- RIGHT: FORM --------
with col2:
    st.markdown("<div class='card' style='padding:2px 10px;'><h3>Send Message</h3>", unsafe_allow_html=True)

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if name and email and message:
            st.success("✅ Message sent successfully!")
        else:
            st.error("⚠️ Please fill all fields")

    st.markdown("</div>", unsafe_allow_html=True)
import streamlit as st

# 🔒 LOGIN CHECK
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Please login first")
    st.stop()

import cv2
import face_recognition
import numpy as np
from PIL import Image
from db import create_tables, add_student, get_students   # ✅ added get_students

create_tables()

st.title("👤 Student Registration")

with st.form("student_form"):
    name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")
    department = st.selectbox("Department", 
        ["Computer Science", "Electronics", "Mechanical", "Civil", "AI & Data Science"])
    course = st.selectbox("Course", ["B.Tech", "M.Tech", "MBA", "PhD"])
    
    submitted = st.form_submit_button("📸 Capture & Register")

if submitted:

    if name == "" or roll_no == "":
        st.warning("⚠️ Fill all fields")
    else:
        st.info("📸 Capturing face...")

        cap = cv2.VideoCapture(0)
        encodings_list = []
        count = 0

        frame_placeholder = st.empty()

        while count < 5:
            ret, frame = cap.read()
            if not ret:
                continue

            rgb_frame = np.array(Image.fromarray(frame).convert("RGB"))

            face_locations = face_recognition.face_locations(rgb_frame)
            encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            if len(encodings) == 1:
                encodings_list.append(encodings[0])
                count += 1
                st.write(f"Captured {count}/5")

            frame_placeholder.image(frame, channels="BGR")

        cap.release()

        if encodings_list:
            avg_encoding = np.mean(encodings_list, axis=0)

            # ✅ -----------------------------
            # DUPLICATE FACE CHECK (NEW PART)
            # -----------------------------
            students = get_students()
            known_encodings = []

            for s in students:
                existing_encoding = np.frombuffer(s[5], dtype=np.float64)
                known_encodings.append(existing_encoding)

            is_duplicate = False

            if len(known_encodings) > 0:
                matches = face_recognition.compare_faces(known_encodings, avg_encoding, tolerance=0.5)
                if True in matches:
                    is_duplicate = True

            # ✅ -----------------------------
            # SAVE ONLY IF NOT DUPLICATE
            # -----------------------------
            if is_duplicate:
                st.error("❌ This face is already registered!")
            else:
                add_student(
                    name,
                    roll_no,
                    department,
                    course,
                    avg_encoding.tobytes()
                )

                st.success(f"✅ {name} registered successfully!")
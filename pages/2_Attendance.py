import cv2
import face_recognition
import numpy as np
import streamlit as st
from db import get_students, mark_attendance, mark_all_absent

# -----------------------------
# Page Title
# -----------------------------
st.title("🎥 Smart Attendance System (Real-Time)")

# -----------------------------
# Course Input (UI only)
# -----------------------------
course_id = st.text_input("📘 Enter Course ID")

lecture_id = st.number_input(
    "🎓 Enter Lecture ID",
    min_value=1,
    step=1,
    value=1
)

# -----------------------------
# Load Students
# -----------------------------
students = get_students()

known_encodings = []
student_ids = []
student_info = {}

for s in students:
    encoding = np.frombuffer(s[5], dtype=np.float64)
    known_encodings.append(encoding)
    student_ids.append(s[0])

    student_info[s[0]] = {
        "name": s[1],
        "roll": s[2]
    }

# -----------------------------
# Tracking
# -----------------------------
attendance_tracker = {}
marked_students = set()

FRAME_THRESHOLD = 5

# -----------------------------
# Session State
# -----------------------------
if "run_camera" not in st.session_state:
    st.session_state.run_camera = False

if "attendance_started" not in st.session_state:
    st.session_state.attendance_started = False

if "marked_list" not in st.session_state:
    st.session_state.marked_list = []

# -----------------------------
# Buttons
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("▶ Start Attendance"):
        if not course_id:
            st.warning("⚠️ Please enter Course ID")
        else:
            st.session_state.run_camera = True

            if not st.session_state.attendance_started:
                mark_all_absent(lecture_id, course_id)  # no change
                st.session_state.attendance_started = True

with col2:
    if st.button("⏹ Stop Attendance"):
        st.session_state.run_camera = False

# -----------------------------
# UI Elements
# -----------------------------
status_box = st.empty()
st.subheader("📋 Attendance Marked:")

# -----------------------------
# CAMERA
# -----------------------------
if st.session_state.run_camera:
    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    while st.session_state.run_camera:
        ret, frame = cap.read()
        if not ret:
            st.error("Camera not working")
            break

        # Resize for speed
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)

        for (top, right, bottom, left), enc in zip(faces, encodings):

            matches = face_recognition.compare_faces(known_encodings, enc, tolerance=0.5)
            face_dist = face_recognition.face_distance(known_encodings, enc)

            label = "Unknown"

            if len(face_dist) > 0:
                best_match_index = np.argmin(face_dist)

                if matches[best_match_index]:
                    student_id = student_ids[best_match_index]
                    info = student_info.get(student_id, {})

                    # Frame tracking
                    if student_id not in attendance_tracker:
                        attendance_tracker[student_id] = 1
                    else:
                        attendance_tracker[student_id] += 1

                    # Mark attendance
                    if (
                        attendance_tracker[student_id] >= FRAME_THRESHOLD
                        and student_id not in marked_students
                    ):
                        mark_attendance(student_id, lecture_id)  # fixed

                        marked_students.add(student_id)

                        name = info.get("name")
                        roll = info.get("roll")
                        entry = f"{name} ({roll})"

                        # Update UI
                        status_box.success(f"✅ {entry} marked present")

                        if entry not in st.session_state.marked_list:
                            st.session_state.marked_list.append(entry)

                    label = f"{info.get('name')} ({info.get('roll')})"

            # Scale back
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2

            # Draw box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, label, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        stframe.image(frame, channels="BGR")

    cap.release()

# -----------------------------
# SHOW MARKED LIST
# -----------------------------
for student in st.session_state.marked_list:
    st.write(f"✅ {student}")
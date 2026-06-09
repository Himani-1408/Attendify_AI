import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Attendance Dashboard")

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
conn = sqlite3.connect("attendify.db")
c = conn.cursor()

# -----------------------------
# LECTURE SELECTION (Improved)
# -----------------------------
lecture_df = pd.read_sql("""
SELECT lecture_id,
       COUNT(*) as records
FROM attendance
GROUP BY lecture_id
""", conn)

st.write(lecture_df)

if lecture_df.empty:
    st.warning("No lectures found in database.")
    st.stop()

lecture_id = st.selectbox("Select Lecture ID", lecture_df["lecture_id"])
st.write("Selected Lecture ID:", lecture_id)

debug_df = pd.read_sql_query(
    "SELECT * FROM attendance WHERE lecture_id=?",
    conn,
    params=(lecture_id,)
)

st.write(debug_df)

# -----------------------------
# TOTAL STUDENTS
# -----------------------------
c.execute("SELECT COUNT(*) FROM students")
total_students = c.fetchone()[0] or 0

# -----------------------------
# PRESENT STUDENTS
# -----------------------------
c.execute("""
SELECT COUNT(*) FROM attendance
WHERE lecture_id=? AND status='Present'
""", (lecture_id,))
present_students = c.fetchone()[0] or 0

# -----------------------------
# ABSENT STUDENTS
# -----------------------------
absent_students = max(total_students - present_students, 0)

# -----------------------------
# PERCENTAGE
# -----------------------------
percentage = (present_students / total_students * 100) if total_students > 0 else 0

# -----------------------------
# DISPLAY METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("👥 Total Students", total_students)
col2.metric("✅ Present", present_students)
col3.metric("📈 Attendance %", f"{percentage:.2f}%")

# -----------------------------
# TABLE
# -----------------------------
st.subheader("📋 Attendance Records")

query = """
SELECT s.name, s.roll_no, 
       COALESCE(a.status, 'Absent') as status
FROM students s
LEFT JOIN attendance a
ON s.id = a.student_id AND a.lecture_id=?
"""

df = pd.read_sql_query(query, conn, params=(lecture_id,))
st.dataframe(df, use_container_width=True)

# -----------------------------
# CHART DATA
# -----------------------------
labels = ["Present", "Absent"]
values = [present_students, absent_students]

# -----------------------------
# BAR CHART
# -----------------------------
st.subheader("📊 Attendance Count")

if sum(values) == 0:
    st.info("No attendance data available.")
else:
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(labels, values, color=["green", "red"])
    ax_bar.set_ylabel("Number of Students")
    st.pyplot(fig_bar)

# -----------------------------
# PIE CHART
# -----------------------------
st.subheader("🥧 Attendance Distribution")

if sum(values) == 0:
    st.warning("No attendance data available for this lecture.")
else:
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(values, labels=labels, autopct='%1.1f%%', colors=["green", "red"])
    ax_pie.axis('equal')
    st.pyplot(fig_pie)

# -----------------------------
# CLOSE CONNECTION
# -----------------------------
conn.close()
import sqlite3
import datetime

DB_NAME = "attendify.db"

# -----------------------------
# CONNECT
# -----------------------------
def connect():
    return sqlite3.connect(DB_NAME)


# -----------------------------
# CREATE TABLES
# -----------------------------
def create_tables():
    conn = connect()
    c = conn.cursor()

    # Students Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll_no TEXT UNIQUE NOT NULL,
        department TEXT,
        course TEXT,
        encoding BLOB
    )
    """)

    # Lectures Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS lectures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course TEXT,
        faculty TEXT,
        start_time TEXT,
        end_time TEXT
    )
    """)

    # Attendance Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        lecture_id INTEGER,
        Course_id TEXT,
        timestamp TEXT,
        status TEXT,
        UNIQUE(student_id, lecture_id)
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# STUDENT FUNCTIONS
# -----------------------------
def add_student(name, roll_no, department, course, encoding):
    conn = connect()
    c = conn.cursor()

    try:
        c.execute("""
        INSERT INTO students (name, roll_no, department, course, encoding)
        VALUES (?, ?, ?, ?, ?)
        """, (name, roll_no, department, course, encoding))

        conn.commit()
        print("✅ Student added")

    except sqlite3.IntegrityError:
        print("❌ Student already exists")

    conn.close()


def get_students():
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT * FROM students")
    data = c.fetchall()

    conn.close()
    return data


# -----------------------------
# LECTURE FUNCTIONS
# -----------------------------
def add_lecture(course, faculty, start_time, end_time):
    conn = connect()
    c = conn.cursor()

    c.execute("""
    INSERT INTO lectures (course, faculty, start_time, end_time)
    VALUES (?, ?, ?, ?)
    """, (course, faculty, start_time, end_time))

    conn.commit()
    conn.close()


def get_lectures():
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT * FROM lectures")
    data = c.fetchall()

    conn.close()
    return data


# -----------------------------
# ATTENDANCE FUNCTIONS
# -----------------------------

# 🔥 STEP 1: Sabko ABSENT mark karo
def mark_all_absent(lecture_id, course_id):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT id FROM students")
    students = c.fetchall()

    for s in students:
        student_id = s[0]

        try:
            c.execute("""
            INSERT INTO attendance
            (student_id, lecture_id, Course_id, timestamp, status)
            VALUES (?, ?, ?, ?, ?)
            """, (
                student_id,
                lecture_id,
                course_id,
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Absent"
            ))
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    conn.close()


# 🔥 STEP 2: Present update karo
def mark_attendance(student_id, lecture_id):
    conn = connect()
    c = conn.cursor()

    c.execute("""
    UPDATE attendance
    SET status = 'Present',
        timestamp = ?
    WHERE student_id = ? AND lecture_id = ?
    """, (
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        student_id,
        lecture_id
    ))

    conn.commit()
    conn.close()


def get_attendance():
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT * FROM attendance")
    data = c.fetchall()

    conn.close()
    return data
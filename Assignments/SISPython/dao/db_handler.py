from util.db_conn_util import DBConnUtil
from datetime import datetime

class DBHandler:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def insert_student(self, student):
        try:
            student.student_id = int(student.student_id)
            student.phone_number = int(student.phone_number)  # Critical for `bigint` type

            # Ensure the date format for date_of_birth
            if isinstance(student.date_of_birth, str):
                student.date_of_birth = datetime.strptime(student.date_of_birth, '%Y-%m-%d').date()

            query = """
                INSERT INTO students (student_id, first_name, last_name, date_of_birth, email, phone_number)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            self.cursor.execute(query, (
                student.student_id,
                student.first_name,
                student.last_name,
                student.date_of_birth,
                student.email,
                student.phone_number
            ))
            self.conn.commit()
            print("Student inserted successfully.")
        except Exception as e:
            print("Failed to insert student:", e)

    def insert_enrollment(self, enrollment):
        try:
            # Check if the student exists before inserting enrollment
            self.cursor.execute("SELECT COUNT(*) FROM students WHERE student_id = ?", (enrollment.student.student_id,))
            student_exists = self.cursor.fetchone()[0]

            if student_exists == 0:
                print(f"Cannot enroll: Student with student_id {enrollment.student.student_id} does not exist.")
                return

            # Proceed to insert the enrollment
            query = """
                INSERT INTO enrollments (enrollment_id, student_id, course_id, enrollment_date)
                VALUES (?, ?, ?, ?)
            """
            self.cursor.execute(query, (
                enrollment.enrollment_id,
                enrollment.student.student_id,
                enrollment.course.course_id,
                enrollment.enrollment_date
            ))
            self.conn.commit()
            print("Enrollment inserted successfully.")
        except Exception as e:
            print("Failed to insert enrollment:", e)

    def insert_payment(self, payment):
        try:
            query = """
                INSERT INTO payments (payment_id, student_id, amount, payment_date)
                VALUES (?, ?, ?, ?)
            """
            self.cursor.execute(query, (
                payment.payment_id,
                payment.student.student_id,
                payment.amount,
                payment.payment_date
            ))
            self.conn.commit()
            print("Payment inserted successfully.")
        except Exception as e:
            print("Failed to insert payment:", e)

    def update_course_teacher(self, course_id, teacher_id):
        try:
            query = "UPDATE courses SET teacher_id = ? WHERE course_id = ?"
            self.cursor.execute(query, (teacher_id, course_id))
            self.conn.commit()
            print("Course teacher updated successfully.")
        except Exception as e:
            print("Failed to update course teacher:", e)

    def close_connection(self):
        self.conn.close()

from util.db_conn_util import DBConnUtil
from entity.enrollment import Enrollment
from entity.payment import Payment

class SISManager:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def add_enrollment(self, student, course, enrollment_date):
        # Check if the student is already enrolled in the course
        self.cursor.execute(
            "SELECT COUNT(*) FROM enrollments WHERE student_id = ? AND course_id = ?",
            (student.student_id, course.course_id)
        )
        if self.cursor.fetchone()[0] > 0:
            print("Student already enrolled in this course.")
            return

        # Insert a new enrollment without specifying enrollment_id (it's auto-generated)
        query = """
            INSERT INTO enrollments (student_id, course_id, enrollment_date)
            VALUES (?, ?, ?)
        """
        self.cursor.execute(query, (
            student.student_id,
            course.course_id,
            enrollment_date
        ))
        self.conn.commit()
        print(f"Enrolled {student.first_name} in {course.course_name}")

    def assign_course_to_teacher(self, course, teacher):
        try:
            self.cursor.execute(
                "UPDATE courses SET teacher_id = ? WHERE course_id = ?",
                (teacher.teacher_id, course.course_id)
            )
            self.conn.commit()
            print(f"Assigned {teacher.first_name} to teach {course.course_name}")
        except Exception as e:
            print(f"Failed to assign teacher to course: {e}")

    def add_payment(self, student, amount, payment_date):
        try:
            # Check if student exists
            self.cursor.execute(
                "SELECT COUNT(*) FROM students WHERE student_id = ?",
                (student.student_id,)
            )
            if self.cursor.fetchone()[0] == 0:
                print(f"Student with ID {student.student_id} does not exist.")
                return

            # Insert payment record
            self.cursor.execute(
                "INSERT INTO payments (student_id, amount, payment_date) VALUES (?, ?, ?)",
                (student.student_id, amount, payment_date)
            )
            self.conn.commit()
            print(f"Recorded payment of ₹{amount} for {student.first_name}")
        except Exception as e:
            print(f"Failed to record payment: {e}")

    def get_enrollments_for_student(self, student):
        try:
            self.cursor.execute(
                "SELECT e.enrollment_id, c.course_name, e.enrollment_date "
                "FROM enrollments e JOIN courses c ON e.course_id = c.course_id "
                "WHERE e.student_id = ?",
                (student.student_id,)
            )
            enrollments = self.cursor.fetchall()  # Fetch all results
            return enrollments
        except Exception as e:
            print(f"Failed to fetch enrollments: {e}")
            return []


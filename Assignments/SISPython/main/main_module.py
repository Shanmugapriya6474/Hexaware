from dao.db_handler import DBHandler
from entity.student import Student
from entity.enrollment import Enrollment
from entity.course import Course
from entity.teacher import Teacher
from entity.payment import Payment
from dao.sis_manager import SISManager

# Step 1: Create DB handler
db = DBHandler()

#  Step 2: Add a new student – John Doe
john = Student(50, "John", "Doe", "1995-08-15", "john.doe@example.com", "123-456-7890")
db.insert_student(john)
print(" John Doe added to students table.")

# Step 3: Add courses
course1 = Course(111, "Introduction to Programming", 4, 1)
course2 = Course(112, "Mathematics 101", 3, 2)

#  Step 4: Enroll John in both courses
enroll1 = Enrollment(32, john, course1, "2025-04-18")
enroll2 = Enrollment(33, john, course2, "2025-04-18")
db.insert_enrollment(enroll1)
db.insert_enrollment(enroll2)
print("John enrolled in two courses.")

#  Task 9 – Assign Sarah Smith to Advanced Database Management
sarah = Teacher(20, "Sarah", "Smith", "sarah.smith@example.com")
new_course = Course(120, "Advanced Database Management", 4, None, "CS302", None)
new_course.assign_teacher(sarah)
print("\n Task 9 – Teacher Assignment")
sarah.display_info()
new_course.display_course_info()
db.update_course_teacher(new_course.course_id, sarah.teacher_id)

#  Task 10 – Jane Johnson makes a payment
jane = Student(43, "Jane", "Johnson", "2000-02-15", "jane.johnson@example.com", "9876543210")
db.insert_student(jane)
payment = Payment(24, jane, 500.00, "2023-04-10")
db.insert_payment(payment)
print("\nTask 10 – Payment Record")
print(f"Student: {jane.first_name} {jane.last_name} | Payment: ₹{payment.amount} | Date: {payment.payment_date}")

#  Task 11 – Enrollment Report for "Computer Science 101"
print("\n Task 11 – Enrollment Report Generation")
sis = SISManager()
cs_course = Course(132, "Computer Science 101", 4)
student1 = Student(204, "Aditi", "Rao", "2002-04-10", "aditi.rao@example.com", "9090909090")
student2 = Student(205, "Rahul", "Verma", "2001-03-15", "rahul.verma@example.com", "8080808080")
sis.add_enrollment(student1, cs_course, "2025-04-21")
sis.add_enrollment(student2, cs_course, "2025-04-21")

print(f"\n Enrollment Report for {cs_course.course_name}:")
for e in cs_course.get_enrollments():
    print(f" Student ID: {e.student.student_id} | Name: {e.student.first_name} {e.student.last_name} | Enrolled on: {e.enrollment_date}")

#  Close DB connection
db.close_connection()

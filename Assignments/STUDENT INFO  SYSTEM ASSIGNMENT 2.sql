create database SISDB
use SISDB
-------------------------------------------------------------TASK1---------------------------------------------------------------------------------------

create table students(student_id int Primary Key,
first_name varchar(20),
last_name varchar(30),
date_of_birth date,
email varchar(30),
phone_number bigint);

create table courses(course_id int Primary Key,
course_name varchar(30),
credits int,
teacher_id int Foreign Key references teacher(teacher_id));

create table enrollments(enrollment_id int Primary Key,
student_id int Foreign Key 
references students(student_id),
course_id int Foreign Key 
references courses(course_id),
enrollment_date date);

create table teacher(teacher_id int Primary Key,
 first_name varchar(30),
last_name varchar(30),
 email varchar(50));

create table payments(payment_id int Primary Key,
student_id int Foreign Key 
references students(student_id),
 amount money,
payment_date date);

insert into students values
(1, 'ram', 'shyam', '1990-05-20', 'ram@gmail.com', 8990935879),
(2, 'eam', 'ali', '1991-05-20', 'eam@gmail.com', 4990935879),
(3, 'qram', 'syed', '1993-05-20', 'qram@gmail.com', 5990935879),
(4, 'kam', 'shin', '1994-05-20', 'kam@gmail.com', 9990935879),
(5, 'lam', 'kim', '1996-05-20', 'lam@gmail.com', 9900935879),
(6, 'som', 'lar', '2000-05-20', 'sam@gmail.com', 8998935879),
(7, 'moe', 'ali', '2020-05-20', 'rmo@gmail.com', 8990935779),
(8, 'virat', 'arora', '1993-05-20', 'virat@gmail.com', 8990635879),
(9, 'smith', 'steve', '2004-05-20', 'smith@gmail.com', 8990435879),
(10, 'rohit', 'thivari', '2000-05-20', 'rohit@gmail.com', 8990935877);

insert into teacher values
(1, 'Ravi', 'Kumar', 'ravi.kumar@school.com'),
(2, 'Anita', 'Sharma', 'anita.sharma@school.com'),
(3, 'David', 'Lee', 'david.lee@school.com'),
(4, 'Priya', 'Menon', 'priya.menon@school.com'),
(5, 'John', 'Smith', 'john.smith@school.com'),
(6, 'Neha', 'Singh', 'neha.singh@school.com'),
(7, 'Michael', 'Brown', 'michael.brown@school.com'),
(8, 'Suresh', 'Reddy', 'suresh.reddy@school.com'),
(9, 'Lakshmi', 'Iyer', 'lakshmi.iyer@school.com'),
(10, 'Daniel', 'Fernandez', 'daniel.fernandez@school.com');
  
insert into courses values
(201, 'Maths', 1, 1),
(202, 'Phys', 2, 3),
(203, 'Chem', 3, 3),
(204, 'Bio', 5, 4),
(205, 'Computer Science', 6, 5),
(206, 'English ', 6, 6),
(207, 'History', 3, 4),
(208, 'Economics', 5, 8),
(209, 'Geography', 4, 9),
(210, ' Science', 3, 4);

insert into enrollments values
(1, 1, 201, '2022-06-10'),
(2, 2, 202, '2022-04-11'),
(3, 3, 203, '2022-06-12'),
(4, 4, 204, '2022-05-13'),
(5, 5, 205, '2022-07-14'),
(6, 6, 206, '2022-06-15'),
(7, 7, 207, '2022-06-16'),
(8, 8, 208, '2022-06-17'),
(9, 9, 209, '2022-06-18'),
(10, 10, 210, '2021-06-19');

insert into payments values
(1, 1, 4800.00, '2022-06-20'),
(2, 2, 4500.00, '2022-04-20'),
(3, 3, 4700.00, '2022-06-18'),
(4, 4, 4600.00, '2022-05-20'),
(5, 5, 5000.00, '2022-07-20'),
(6, 6, 4900.00, '2022-06-22'),
(7, 7, 4600.00, '2022-06-25'),
(8, 8, 5100.00, '2022-06-27'),
(9, 9, 5200.00, '2022-06-29'),
(10, 10, 5300.00, '2021-06-25');

-----------------------------------------------------------------------TASK2----------------------------------------------------------------------
----1.Write an SQL query to insert a new student into the "Students" table
 insert into students values 
 (11, 'john', 'doe', '1995-08-15',
 'john.doe@example.com', 1234567890);

----2.Write an SQL query to enroll a student in a course.
insert into enrollments (enrollment_id, 
student_id, course_id, enrollment_date)
values
(12, 5, 205, '2024-06-01'); 

---3.Update the email address of a specific teacher in the "Teacher" table.
update teacher
set email = 'david.lee_updated@school.com'
where teacher_id = 3;

--4. Write an SQL query to delete a specific enrollment record from the "Enrollments" table  based on the student and course*/
delete from enrollments
where student_id = 5 
and course_id = 205;

--5.Update the "Courses" table to assign a specific teacher to a course.
update courses
set teacher_id = 3
where course_id = 204;

--6.Delete a specific student from the "Students" table and remove all their enrollment records from the "Enrollments" table.
begin transaction;
delete from payments
where student_id = 5;
delete from enrollments
where student_id = 5;
delete from students
where student_id = 5;
commit;

--7.Update the payment amount for a specific payment record in the "Payments" table.
update payments
set amount = 5500.00
where payment_id = 3;

----------------------------------------------------------------------TASK3-----------------------------------------------------------

--1.Write an sql query to calculate the total payments made by a specific student.
select s.first_name, s.last_name,
sum(p.amount) as total_payments
from students s
join payments p on s.student_id = p.student_id
where s.student_id = 3
group by s.first_name, s.last_name;

--2.Write an sql query to retrieve a list of courses along with the count of students enrolled in each course.
select c.course_name, count(e.student_id) as student_count
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_name;

--3.Write an SQL query to find the names of students who have not enrolled in any course.
select s.first_name, s.last_name
from students s
left join enrollments e on s.student_id = e.student_id
where e.enrollment_id is null;

--4.Write a query to retrieve the first name, last name of students, and the names of the courses they are enrolled in.
select s.first_name, s.last_name, c.course_name
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id;

--5.Create a query to list the names of teachers and the courses they are assigned to.Join the "Teacher" table with the "Courses" table.
select t.first_name, t.last_name, c.course_name
from teacher t
join courses c on t.teacher_id = c.teacher_id;

--6.Retrieve a list of students and their enrollment dates for a specific course .
select s.first_name, s.last_name, e.enrollment_date, c.course_name
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id
where c.course_name = 'maths';

--7.Find the names of students who have not made any payments.
select s.first_name, s.last_name
from students s
left join payments p on s.student_id = p.student_id
where p.payment_id is null;

--8.Write a query to identify courses that have no enrollments.
select c.course_name
from courses c
left join enrollments e on c.course_id = e.course_id
where e.enrollment_id is null;

---9.Identify students who are enrolled in more than one course using self join.
select distinct s1.student_id, st.first_name, st.last_name
from enrollments s1
join enrollments s2 on s1.student_id = s2.student_id and s1.course_id <> s2.course_id
join students st on s1.student_id = st.student_id;

---10.Find teachers who are not assigned to any courses.
select t.teacher_id, t.first_name, t.last_name, t.email
from teacher t
left join courses c on t.teacher_id = c.teacher_id
where c.course_id is null;

-------------------------------------------------------------------------------TASK4---------------------------------------------------------------

---1.Write a query to calculate the average number of students enrolled in each course.
select avg(student_count) as average_students_per_course
from (
  select course_id, count(student_id) as student_count
  from enrollments
  group by course_id
) as course_enrollments;

--2.Identify the student(s) who made the highest payment.
select s.first_name, s.last_name, p.amount
from payments p
join students s on s.student_id = p.student_id
where p.amount = (
  select max(amount) 
  from payments);

--3.Retrieve a list of courses with the highest number of enrollment.
select c.course_name, count(e.enrollment_id) as total_enrollments
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name
having count(e.enrollment_id) = (
  select max(course_count)
  from (
    select course_id,count(enrollment_id) as course_count
    from enrollments
    group by course_id
  ) as sub);

--4.Calculate the total payments made to courses taught by each teacher.
select t.teacher_id, t.first_name, t.last_name, 
       (select sum(p.amount)
        from enrollments e
        join payments p on e.student_id = p.student_id
        where e.course_id in (
            select c.course_id
            from courses c
            where c.teacher_id = t.teacher_id)) 
			as total_payments from teacher t;

--5.Identify students who are enrolled in all available courses.
select s.student_id, s.first_name, s.last_name
from students s
where (
  select count(distinct e.course_id)
  from enrollments e
  where e.student_id = s.student_id) =
  (select count(*)from courses);

--6.Retrieve the names of teachers who have not been assigned to any course.
select first_name, last_name
from teacher
where teacher_id not in (
  select distinct teacher_id
  from courses);

--7.Calculate the average age of all students.
select avg(age) as average_age
from (
  select datediff(year, date_of_birth, getdate()) as age
  from students
) as age_table;

--8.Identify courses with no enrollments.
select course_name
from courses
where course_id not in (
  select course_id from enrollments);

--9.Calculate the total payments made by each student for each course they are enrolled in.
select e.student_id, e.course_id, 
       (select sum(p.amount)
        from payments p
        where p.student_id = e.student_id
       ) as total_payment
from enrollments e
group by e.student_id, e.course_id;

--10.Identify students who have made more than one payment.
select s.student_id, s.first_name, s.last_name
from students s
where s.student_id in (
  select student_id
  from payments
  group by student_id
  having count(*) > 1);

--11.Write an sql query to calculate the total payments made by each student.
select s.student_id, s.first_name, s.last_name, 
sum(p.amount) as total_payments
from students s
join payments p on s.student_id = p.student_id
group by s.student_id, 
s.first_name, s.last_name;

--12.Retrieve a list of course names along with the count of students enrolled in each course.
select c.course_name, count(e.student_id) as student_count
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_name;

--13.Calculate the average payment amount made by students.
select s.first_name, s.last_name, avg(p.amount) as average_payment
from students s
join payments p on s.student_id = p.student_id
group by s.first_name, s.last_name;
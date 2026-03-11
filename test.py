from datetime import datetime

from db.models import Base
from db.session import engine, get_session
from db.services import (
    TeacherService,
    UserService,
    CourseService,
    GroupService,
    StudentService,
    LessonService,
    PaymentService,
)


session = get_session()

course_service = CourseService(session=session)
group_service = GroupService(session=session)
lesson_service = LessonService(session=session)
user_service = UserService(session=session)
teacher_service = TeacherService(session=session)
student_service = StudentService(session=session)
payment_service = PaymentService(session=session)


def create_tables():
    Base.metadata.create_all(bind=engine)


def main():
    # Create users
    user1 = user_service.register(
        username="admin", password="password123", role="admin"
    )
    user2 = user_service.register(
        username="Boburjon", password="password123", role="teacher"
    )
    user3 = user_service.register(
        username="user1", password="password123", role="student"
    )
    user4 = user_service.register(
        username="john", password="password123", role="student"
    )
    user5 = user_service.register(
        username="maria", password="password123", role="student"
    )
    user6 = user_service.register(
        username="lisa", password="password123", role="student"
    )
    user7 = user_service.register(
        username="david", password="password123", role="student"
    )
    user8 = user_service.register(
        username="sara", password="password123", role="student"
    )
    user9 = user_service.register(
        username="michael", password="password123", role="student"
    )
    user10 = user_service.register(
        username="emma", password="password123", role="student"
    )
    user11 = user_service.register(
        username="oliver", password="password123", role="student"
    )
    user12 = user_service.register(
        username="ava", password="password123", role="student"
    )

    # create student and teacher
    student1 = student_service.create_student(
        user=user3, first_name="sami", last_name="samiyev", phone="1234567890"
    )
    student2 = student_service.create_student(
        user=user4, first_name="alex", last_name="alexyev", phone="1234567890"
    )
    student3 = student_service.create_student(
        user=user5, first_name="maria", last_name="mariyev", phone="1234567890"
    )
    student4 = student_service.create_student(
        user=user6, first_name="lisa", last_name="lisayeva", phone="1234567890"
    )
    student5 = student_service.create_student(
        user=user7, first_name="david", last_name="davidyev", phone="1234567890"
    )
    student6 = student_service.create_student(
        user=user8, first_name="sara", last_name="sarayeva", phone="1234567890"
    )
    student7 = student_service.create_student(
        user=user9, first_name="michael", last_name="michayev", phone="1234567890"
    )
    student8 = student_service.create_student(
        user=user10, first_name="emma", last_name="emmayeva", phone="1234567890"
    )
    student9 = student_service.create_student(
        user=user11, first_name="oliver", last_name="olivyev", phone="1234567890"
    )
    student10 = student_service.create_student(
        user=user12, first_name="ava", last_name="avayeva", phone="1234567890"
    )

    teacher1 = teacher_service.create_teacher(
        user=user2,
        first_name="vali",
        last_name="valiyev",
        email="vali@example.com",
        specialization="Python",
    )

    # create course
    course1 = course_service.create_course(
        name="Python Programming", description="Learn Python from scratch.", price=100.0
    )
    course2 = course_service.create_course(
        name="Data Science", description="Learn Data Science with Python.", price=150.0
    )

    # create group
    group1 = group_service.create_group(name="Python N10", course=course1, capacity=20)
    group2 = group_service.create_group(name="SMM N13", course=course2, capacity=15)

    # assign teacher to group
    teacher_service.assign_group(group=group1, teacher=teacher1)

    # enroll student to group
    student_service.enroll_group(student=student1, group=group1)
    student_service.enroll_group(student=student2, group=group1)
    student_service.enroll_group(student=student3, group=group1)
    student_service.enroll_group(student=student4, group=group1)
    student_service.enroll_group(student=student5, group=group1)
    student_service.enroll_group(student=student6, group=group1)
    student_service.enroll_group(student=student7, group=group1)
    student_service.enroll_group(student=student8, group=group1)
    student_service.enroll_group(student=student9, group=group1)
    student_service.enroll_group(student=student10, group=group1)

    # make payment
    payment1 = student_service.make_payment(
        student=student1, group=group1, amount=100.0
    )
    payment2 = student_service.make_payment(
        student=student2, group=group1, amount=100.0
    )
    payment3 = student_service.make_payment(
        student=student3, group=group1, amount=100.0
    )
    payment4 = student_service.make_payment(
        student=student4, group=group1, amount=100.0
    )
    payment5 = student_service.make_payment(
        student=student5, group=group1, amount=100.0
    )
    payment6 = student_service.make_payment(
        student=student6, group=group1, amount=100.0
    )
    payment7 = student_service.make_payment(
        student=student7, group=group1, amount=100.0
    )
    payment8 = student_service.make_payment(
        student=student8, group=group1, amount=100.0
    )
    payment9 = student_service.make_payment(
        student=student9, group=group1, amount=100.0
    )
    payment10 = student_service.make_payment(
        student=student10, group=group1, amount=100.0
    )

    # create lesson
    lesson1 = teacher_service.create_lesson(
        group=group1,
        teacher=teacher1,
        date=datetime(2026, 1, 3),
        topic="Introduction to Python",
    )
    lesson2 = teacher_service.create_lesson(
        group=group1,
        teacher=teacher1,
        date=datetime(2026, 1, 8),
        topic="Data Types and Variables",
    )
    lesson3 = teacher_service.create_lesson(
        group=group1, teacher=teacher1, date=datetime(2026, 1, 15), topic="Control Flow"
    )
    lesson4 = teacher_service.create_lesson(
        group=group1,
        teacher=teacher1,
        date=datetime(2026, 1, 22),
        topic="Functions and Modules",
    )
    lesson5 = teacher_service.create_lesson(
        group=group1,
        teacher=teacher1,
        date=datetime(2026, 1, 29),
        topic="Object-Oriented Programming",
    )
    lesson6 = teacher_service.create_lesson(
        group=group1, teacher=teacher1, date=datetime(2026, 2, 5), topic="File Handling"
    )
    lesson7 = teacher_service.create_lesson(
        group=group1,
        teacher=teacher1,
        date=datetime(2026, 2, 12),
        topic="Error Handling and Exceptions",
    )


if __name__ == "__main__":
    main()

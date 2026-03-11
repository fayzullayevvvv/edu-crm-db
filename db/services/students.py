from sqlalchemy import select, join
from sqlalchemy.orm import Session

from db.models import User, Student, UserRole, Group, Payment, Course, Enrollment


class StudentService:
    def __init__(self, session: Session):
        self.session = session

    def create_student(
        self, user: User, first_name: str, last_name: str, phone: str
    ) -> Student:
        if user.role != UserRole.STUDENT:
            raise ValueError("user role is not student")
        if user.student_profile:
            raise ValueError("student already exists.")

        student = Student(
            first_name=first_name, last_name=last_name, phone=phone, user=user
        )

        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def register(
        self, user: User, first_name: str, last_name: str, phone: str
    ) -> Student:
        if user.role != UserRole.STUDENT:
            raise ValueError("user role is not student.")
        if user.student_profile:
            raise ValueError("student already exists.")

        student = Student(
            first_name=first_name, last_name=last_name, phone=phone, user=user
        )
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def enroll_group(self, student: Student, group: Group) -> Student:
        if group in student.groups:
            raise ValueError("Student is already enrolled in this group.")

        student.groups.append(group)

        self.session.commit()
        self.session.refresh(student)
        return student

    def make_payment(self, student: Student, group: Group, amount: float) -> Payment:
        payment = Payment(student_id=student.id, group_id=group.id, amount=amount)

        self.session.add(payment)
        self.session.commit()
        self.session.refresh(payment)
        return payment

    def view_courses(self, student: Student) -> list[Course]:
        stmt = (
            select(Course)
            .join(Group, Course.id == Group.course_id)
            .join(Enrollment, Group.id == Enrollment.group_id)
            .where(Enrollment.student_id == student.id)
        )
        return self.session.execute(stmt).scalar().all

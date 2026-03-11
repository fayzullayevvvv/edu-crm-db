from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import Group, Course, GroupStatus, Student, Enrollment


class GroupService:
    def __init__(self, session: Session):
        self.session = session

    def create_group(self, course: Course, capacity: int) -> Group:
        group = Group(course_id=course.id, capacity=capacity, status=GroupStatus.ACTIVE)
        self.session.add(group)
        self.session.commit()
        self.session.refresh(group)
        return group

    def add_student(self, student: Student, group: Group) -> Student:
        for e in group.enrollments:
            if e.student_id == student.id:
                raise ValueError("Student already enrolled in this group")

        if len(group.enrollments) >= group.capacity:
            raise ValueError("Group is full. Cannot enroll more students.")
        
        enrollment = Enrollment(student_id=student.id, group_id=group.id)
        self.session.add(enrollment)
        self.session.commit()
        self.session.refresh(enrollment)
        return student

    def remove_student(self, student: Student, group: Group) -> Student:
        enrollment = (
            self.session.query(Enrollment)
            .filter_by(student_id=student.id, group_id=group.id)
            .first()
        )
        if not enrollment:
            raise ValueError("Student not enrolled in this group.")
        
        self.session.delete(enrollment)
        self.session.commit()
        print("student deleted successfully.")
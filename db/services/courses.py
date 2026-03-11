from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models.course import Course


class CourseService:
    def __init__(self, session: Session):
        self.session = session

    def create_course(self, name: str, description: str, price: float) -> Course:
        existing_course = self.get_course_by_name(name)
        if existing_course:
            raise ValueError("course already exists.")
        
        course = Course(
            name=name,
            description=description,
            price=price
        )
        self.session.add(course)
        self.session.commit()
        return course

    def update_course(self, course: Course, name: str, description: str, price: float):
        existing_course = self.get_course_by_id(id)
        if existing_course and existing_course.id != course.id:
            raise ValueError("course already exists.")
        
        course.name = name
        course.description = description
        course.price = price

        self.session.add(course)
        self.session.commit()
        self.session.refresh(course)
        return course

    def delete_course(self, course: Course):
        existing_course = self.get_course_by_id(id)
        if not existing_course:
            raise ValueError("course not found.")

        self.session.delete(course)
        self.session.commit()
        print("course deleted successfully.")

    def get_course_by_name(self, name: str) -> Course | None:
        stmt = select(Course).where(Course.name == name)
        return self.session.execute(stmt).scalar_one_or_none()
    
    def get_course_by_id(self, id: int) -> Course | None:
        stmt = select(Course).where(Course.id == id)
        return self.session.execute(stmt).scalar_one_or_none()
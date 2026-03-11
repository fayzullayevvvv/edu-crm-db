from datetime import date

from sqlalchemy.orm import Session

from ..models import Lesson, Group, Teacher


class LessonService:
    def __init__(self, session: Session):
        self.session = session

    def schedule_lesson(
        self,
        group: Group,
        teacher: Teacher,
        date: date,
        topic: str = None,
    ) -> Lesson:
        existing_lesson = self.get_lesson_by_date(group_id=group.id, date=date)

        if existing_lesson:
            raise ValueError("Lesson already scheduled for this date.")

        lesson = Lesson(
            group_id=group.id, teacher_id=teacher.id, date=date, topic=topic
        )

        self.session.add(lesson)
        self.session.commit()
        self.session.refresh(lesson)

        return lesson

    def update_lesson(
        self,
        group: Group,
        teacher: Teacher,
        date: date,
        topic: str = None,
    ) -> Lesson:
        existing_lesson = self.get_lesson_by_date(group_id=group.id, date=date)

        if not existing_lesson:
            raise ValueError("Lesson not found for this date.")

        existing_lesson.teacher_id = teacher.id
        existing_lesson.topic = topic

        self.session.add(existing_lesson)
        self.session.commit()
        self.session.refresh(existing_lesson)

        return existing_lesson

    def cancel_lesson(
        self,
        group: Group,
        date: date,
    ) -> None:
        existing_lesson = self.get_lesson_by_date(group_id=group.id, date=date)

        if not existing_lesson:
            raise ValueError("Lesson not found for this date.")

        self.session.delete(existing_lesson)
        self.session.commit()
        print("lesson deleted successfully.")

    def get_lesson_by_date(self, group_id: int, date: date) -> Lesson | None:
        return (
            self.session.query(Lesson).filter_by(group_id=group_id, date=date).first()
        )

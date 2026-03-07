from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

from .base import Base, TimestampMixin


class GroupStatus:
    PANDING = "ochilyotgan"
    ACTIVE = "aktiv"
    CLOSED = "yopilgan"
    GRADUATED = "bitirgan"


class Group(Base, TimestampMixin):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    course_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("courses.id"), nullable=False
    )
    teacher_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("teachers.id"), nullable=False
    )
    capacity: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[str] = mapped_column(String(30))

    course: Mapped["Course"] = relationship("Course", back_populates="groups")
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="groups")
    enrollments: Mapped["Enrollment"] = relationship(
        "Enrollment", back_populates="group"
    )
    lessons: Mapped[list["Lesson"]] = relationship("Lesson", back_populates="group")
    payments: Mapped[list["Payment"]] = relationship("Payment", back_populates="group")


class Enrollment(Base, TimestampMixin):
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("students.id"), nullable=False
    )
    group_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("groups.id"), nullable=False
    )

    student: Mapped["Student"] = relationship("Student", back_populates="enrollments")
    group: Mapped["Group"] = relationship("Group", back_populates="enrollments")

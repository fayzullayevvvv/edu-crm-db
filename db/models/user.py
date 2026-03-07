from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

from .base import Base, TimestampMixin


class UserRole:
    ADMIN = "admin"
    STUDENT = "student"
    TEACHER = "teacher"


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)

    student_profile: Mapped["Student"] = relationship(
        "Student", uselist=False, back_populates="user"
    )
    teacher_profile: Mapped["Teacher"] = relationship(
        "Teacher", uselist=False, back_populates="user"
    )


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user: Mapped[User] = relationship("User", back_populates="student_profile")
    enrollments: Mapped["Enrollment"] = relationship(
        "Enrollment", back_populates="student"
    )
    payments: Mapped[list["Payment"]] = relationship(
        "Payment", back_populates="student"
    )


class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=True)
    specialization: Mapped[str] = mapped_column(String(255), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user: Mapped[User] = relationship("User", back_populates="teacher_profile")
    groups: Mapped[list["Group"]] = relationship("Group", back_populates="teacher")

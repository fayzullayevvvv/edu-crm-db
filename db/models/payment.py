from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, ForeignKey

from .base import Base, TimestampMixin


class Payment(Base, TimestampMixin):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("students.id"), nullable=False
    )
    group_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("groups.id"), nullable=False
    )
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    student: Mapped["Student"] = relationship("Student", back_populates="payments")
    group: Mapped["Group"] = relationship("Group", back_populates="payments")

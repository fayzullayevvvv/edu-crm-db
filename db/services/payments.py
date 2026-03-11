from sqlalchemy.orm import Session

from ..models import Payment, Student, Group


class PaymentService:
    def __init__(self, session: Session):
        self.sessinon = session

    def make_payment(self, student: Student, group: Group, amount: float) -> Payment:
        payment = Payment(student_id=student.id, group_id=group.id, amount=amount)
        self.session.add(payment)
        self.sessinon.commit()
        self.sessinon.refresh(payment)
        return payment

    def refund_payment(self, payment: Payment) -> None:
        existing_payment = self.get_payment_by_id(payment.id)

        if not existing_payment:
            raise ValueError("Payment not found.")

        self.session.delete(payment)
        self.session.commmit()
        print("payment deleted successfully")

    def get_payment_by_id(self, id: int) -> Payment:
        return self.sessinon.query(Payment).filter_by(id=id).first()

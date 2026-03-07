from sqlalchemy.orm import Session

from db.models import User, UserRole
from db.utils.hashing import hash_password


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def register(self, username: str, password: str, role: str) -> User:
        existing_user = self.session.query(User).filter_by(username=username).first()
        if existing_user:
            raise ValueError("username already exists.")

        if role not in (UserRole.ADMIN, UserRole.STUDENT, UserRole.TEACHER):
            raise ValueError("role not found.")

        user = User(
            username=username, hashed_password=hash_password(password), role=role
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user_by_username(self, username: str) -> User | None:
        return self.session.query(User).filter_by(username=username).first()

    def valid_password(self, user: User, password: str) -> bool:
        return user.hashed_password == hash_password(password)

    def authenticate(self, username: str, password: str) -> User | None:
        user = self.get_user_by_username(username)
        if not user:
            return None

        if self.valid_password(user, password):
            return user

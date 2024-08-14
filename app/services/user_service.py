from app.repositories.user_repository import UserRepository
from app.models.user import User


class UserService:
    def __init__(self):
        self._user_repository = UserRepository()

    def create_user(self, name: str, email: str) -> User:
        user_id = len(self._user_repository._users) + 1
        new_user = User(user_id=user_id, email=email, name=name)
        return self._user_repository.add_user(new_user)
    
    def get_user(self, user_id: int) -> User:
        return self._user_repository.get_user(user_id)
    
    def update_user(self, user_id: int, name: str, email: str) -> User:
        user = self._user_repository.get_user(user_id)
        if user:
            user.name = name
            user.email = email
            return self._user_repository.update_user(user)
        return None
    
    def delete_user(self, user_id: int) -> bool:
        return self._user_repository.delete_user(user_id)

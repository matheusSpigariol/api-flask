from app.repositories.user.user_repository import UserRepository
from app.models.user import User


class UserService:
    def __init__(self):
        self._user_repository = UserRepository()

    def register_user(self, request_data) -> None:
        name = request_data.name
        email = request_data.email
        
        return self._user_repository.create_user(name, email)
    
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

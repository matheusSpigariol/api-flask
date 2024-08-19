from app.models.user import User


class UserRepository:
    def __init__(self) -> None:
        self._users = {}

    def add_user(self, user: User) -> User:
        self._users[user.id] = user
        return user
    
    def get_user(self, user_id: int) -> User:
        return self._users.get(user_id)
    
    def update_user(self, user: User) -> User:
        if user.id in self._users:
            self._users[user.id] = user
            return user
        return None
    
    def delete_user(self, user_id: int) -> bool:
       return self._users.pop(user_id, None) is not None 
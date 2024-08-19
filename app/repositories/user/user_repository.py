from app.models.user import User
from app.repositories.user import queries


class UserRepository:
    def __init__(self) -> None:
        self._users = {},
        self._queries = queries

    def add_user(self, user: User) -> User:
        self._users[user.id] = user
        return user
    
    def get_user(self, user_id: int) -> User:
        db_user = self._queries.get_user(user_id)
        return User(
            user_id=db_user['id'],
            name=db_user['nome'],
            email=db_user['email']
        )
    
    def update_user(self, user: User) -> User:
        if user.id in self._users:
            self._users[user.id] = user
            return user
        return None
    
    def delete_user(self, user_id: int) -> bool:
       return self._users.pop(user_id, None) is not None 
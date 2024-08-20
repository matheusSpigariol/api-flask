from app.responses import ResponseCodes
from app.exception.custom_erros import UserNotFound
from app.models.user import User
from app.repositories.user import queries


class UserRepository:
    def __init__(self) -> None:
        self._users = {},
        self._queries = queries

    def create_user(self, name, email) -> None:
        return self._queries.add_new_user(name, email)
    
    def get_user(self, user_id: int) -> User:
        db_user = self._queries.get_user(user_id)
        if not db_user:
            raise UserNotFound("User not found", status=ResponseCodes.NOT_FOUND)
        
        return User(
            user_id=db_user['id'],
            name=db_user['name'],
            email=db_user['email']
        )
    
    def update_user(self, user: User) -> User:
        if user.id in self._users:
            self._users[user.id] = user
            return user
        return None
    
    def delete_user(self, user_id: int) -> bool:
       return self._users.pop(user_id, None) is not None 
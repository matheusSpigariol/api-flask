class User:
    def __init__(self, user_id: int , name: str, email: str) -> None:
        self._id = user_id
        self._name = name
        self._email = email

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email: str):
        self._email = email

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

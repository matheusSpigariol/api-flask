class CustomErrors(Exception):
    def __init__(self, message, extra=None, status=None) -> None:
        self._message = message
        self._extra = extra
        if status: self._status = status
        super().__init__(message)

class UserNotFound(CustomErrors):
    pass

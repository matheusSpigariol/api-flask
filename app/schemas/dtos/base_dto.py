class BaseDTO:
    def as_dict(self):
        return self.__dict__
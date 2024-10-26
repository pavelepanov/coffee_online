from src.domain.common.errors import ValueObjectValidationError
from src.domain.common.value_object import ValueObject


class UserHashedPassword(ValueObject):
    def __init__(self, hashed_password: str):
        self.__hashed_password = hashed_password

    def _validate(self) -> None:
        if not isinstance(self.__hashed_password, str):
            raise ValueObjectValidationError("User password must be a str")
        if len(self.__hashed_password) > 1024:
            raise ValueObjectValidationError(
                "Hashed password must be less then 1024 symbols"
            )

    @property
    def password(self):
        return self.__password

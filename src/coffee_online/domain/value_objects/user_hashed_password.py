from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject


class UserHashedPassword(ValueObject):
    def __init__(self, hashed_password: str):
        self.__hashed_password = hashed_password
        self._validate()

    def _validate(self) -> None:
        if not isinstance(self.__hashed_password, str):
            raise ValueObjectValidationError("User password must be a str")
        if len(self.__hashed_password) > 1024:
            raise ValueObjectValidationError(
                "Hashed password must be less then 1024 symbols"
            )

    @property
    def hashed_password(self):
        return self.__hashed_password

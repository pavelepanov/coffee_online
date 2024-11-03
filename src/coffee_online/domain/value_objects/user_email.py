from re import match

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject


class UserEmail(ValueObject):
    def __init__(self, email: str):
        self.__email = email
        self._validate()

    def _validate(self) -> None:
        email_pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"

        if not isinstance(self.__email, str):
            raise ValueObjectValidationError("User email must be a str")

        if not isinstance(self.__email, str):
            raise ValueObjectValidationError("User email must be an str")
        if not match(email_pattern, self.__email):
            raise ValueObjectValidationError(
                "Invalid email format. User email must be in the format 'example@example.com'."
            )
        if len(self.__email) > 320:
            raise ValueObjectValidationError(
                "User email must be less than 320 symbols"
            )

    @property
    def email(self):
        return self.__email

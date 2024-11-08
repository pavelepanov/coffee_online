import logging

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)

class UserHashedPassword(ValueObject):
    def __init__(self, hashed_password: str):
        self.__hashed_password = hashed_password
        self._validate()

    def _validate(self) -> None:
        try:
            if not isinstance(self.__hashed_password, str):
                raise ValueObjectValidationError("User hashed password must be a str")
            if len(self.__hashed_password) > 1024:
                raise ValueObjectValidationError(
                    "Hashed password must be less then 1024 symbols"
                )
        except Exception as e:
            logging.exception("User hashed password did not create because %s" % e)

    @property
    def hashed_password(self):
        return self.__hashed_password

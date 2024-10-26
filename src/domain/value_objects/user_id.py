from src.domain.common.value_object import ValueObject
from src.domain.common.errors import ValueObjectValidationError


class UserId(ValueObject):
    def __init__(self, id: int):
        self.__id = id

    def _validate(self) -> None:
        if not isinstance(self.__id, int):
            raise ValueObjectValidationError('User id must be an int')

    @property
    def id(self):
        return self.__id

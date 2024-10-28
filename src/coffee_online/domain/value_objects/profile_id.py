from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject


class ProfileId(ValueObject):
    def __init__(self, id: int):
        self.__id = id

    def _validate(self) -> None:
        if not isinstance(self.__id, int):
            raise ValueObjectValidationError("Profile id must be an int")

    @property
    def id(self):
        return self.__id

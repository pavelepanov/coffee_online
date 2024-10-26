from src.domain.common.value_object import ValueObject
from src.domain.common.errors import ValueObjectValidationError


class UserName(ValueObject):
    def __init__(self, name: str):
        self.__name = name

    def _validate(self) -> None:
        ru_letters = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                      "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я")

        if not isinstance(self.__name, str):
            raise ValueObjectValidationError('Name must be str"')
        if len(self.__name) > 50:
            raise ValueObjectValidationError('User name must be less than 50 letters')
        if len(self.__name) <= 0:
            raise ValueObjectValidationError('User name must be greater than 0 letters')
        if not set(self.__name.lower()).issubset(ru_letters):
            raise ValueObjectValidationError('User name must be russian')

    @property
    def name(self):
        return self.__name

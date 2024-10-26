from src.domain.common.errors import ValueObjectValidationError
from src.domain.common.value_object import ValueObject


class UserSex(ValueObject):
    def __init__(self, sex: str):
        self.__sex = sex

    def _validate(self) -> None:
        sex = ('male', 'female')

        if not isinstance(self.__sex, str):
            raise ValueObjectValidationError('User sex must be str')
        if self.__sex not in sex:
            raise ValueObjectValidationError('User sex must be like Male or Female')

    @property
    def sex(self):
        return self.__sex

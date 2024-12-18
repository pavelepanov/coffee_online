import logging

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)

class ProfileSex(ValueObject):
    def __init__(self, sex: str):
        self.__sex = sex
        self._validate()

    def _validate(self) -> None:
        try:
            sex = ("male", "female")

            if not isinstance(self.__sex, str):
                raise ValueObjectValidationError("Profile sex must be str")
            if self.__sex.lower() not in sex:
                raise ValueObjectValidationError(
                    "Profile sex must be like Male or Female"
                )
        except Exception as e:
            logging.exception("Profile sex did not create because %s" % e)

    @property
    def sex(self):
        return self.__sex

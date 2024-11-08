import logging

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)

class ProfileName(ValueObject):
    def __init__(self, name: str):
        self.__name = name
        self._validate()

    def _validate(self) -> None:
        try:
            ru_letters = (
                "а",
                "б",
                "в",
                "г",
                "д",
                "е",
                "ё",
                "ж",
                "з",
                "и",
                "й",
                "к",
                "л",
                "м",
                "н",
                "о",
                "п",
                "р",
                "с",
                "т",
                "у",
                "ф",
                "х",
                "ц",
                "ч",
                "ш",
                "щ",
                "ъ",
                "ы",
                "ь",
                "э",
                "ю",
                "я",
            )

            if not isinstance(self.__name, str):
                raise ValueObjectValidationError("Profile name must be str")
            if len(self.__name) > 50:
                raise ValueObjectValidationError(
                    "Profile name must be less than 50 letters"
                )
            if len(self.__name) <= 0:
                raise ValueObjectValidationError(
                    "Profile name must be greater than 0 letters"
                )
            if not set(self.__name.lower()).issubset(ru_letters):
                raise ValueObjectValidationError("Profile name must be russian")
        except Exception as e:
            logging.exception("Profile name did not create because %s" % e)

    @property
    def name(self):
        return self.__name

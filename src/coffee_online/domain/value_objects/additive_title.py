import logging

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)


class AdditiveTitle(ValueObject):
    def __init__(self, title: str):
        self.__title = title
        self._validate()

    def _validate(self) -> None:
        try:
            if not isinstance(self.__title, str):
                raise ValueObjectValidationError("Additive title must be a str")
        except Exception as e:
            logging.exception("Additive title did not create because %s" % e)

    @property
    def title(self):
        return self.__title

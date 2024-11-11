import logging

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)


class CoffeeDescription(ValueObject):
    def __init__(self, description: str):
        self.__description= description
        self._validate()

    def _validate(self) -> None:
        try:
            if not isinstance(self.__description, str):
                raise ValueObjectValidationError("Coffee description must be a str")
        except Exception as e:
            logging.exception("Coffee description did not create because %s" % e)

    @property
    def description(self):
        return self.__description

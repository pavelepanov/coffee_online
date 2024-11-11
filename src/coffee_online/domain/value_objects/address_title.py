import logging

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)


class AddressTitle(ValueObject):
    def __init__(self, title: str):
        self.__id = title
        self._validate()

    def _validate(self) -> None:
        try:
            if not isinstance(self.__id, str):
                raise ValueObjectValidationError("Address title must be a str")
        except Exception as e:
            logging.exception("Address title did not create because %s" % e)

    @property
    def id(self):
        return self.__id

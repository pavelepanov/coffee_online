import logging

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)


class OrderId(ValueObject):
    def __init__(self, id: int):
        self.__id = id
        self._validate()

    def _validate(self) -> None:
        try:
            if not isinstance(self.__id, int):
                raise ValueObjectValidationError("Address id must be an int")
        except Exception as e:
            logging.exception("Address id did not create because %s" % e)

    @property
    def id(self):
        return self.__id

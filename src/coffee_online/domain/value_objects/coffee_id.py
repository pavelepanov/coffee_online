import logging

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)


class AddressId(ValueObject):
    def __init__(self, time: int):
        self.__time = time
        self._validate()

    def _validate(self) -> None:
        times = [5, 10, 15, 30]

        try:
            if not isinstance(self.__time, int):
                raise ValueObjectValidationError("Time must be an int")
            if self.__time not in times:
                raise ValueObjectValidationError("Time must be in [5, 10, 15, 30] minutes")
        except Exception as e:
            logging.exception("Time did not create because %s" % e)

    @property
    def time(self):
        return self.__time

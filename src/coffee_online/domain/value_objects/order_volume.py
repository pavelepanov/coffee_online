import logging

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)


class OrderVolume(ValueObject):
    def __init__(self, volume: str):
        self.__volume = volume
        self._validate()

    def _validate(self) -> None:
        volumes = ["small", "medium", "large", ]

        try:
            if not isinstance(self.__volume, str):
                raise ValueObjectValidationError("Order volume must be a str")
            if self.__volume not in volumes:
                raise ValueObjectValidationError("Order volume must be in [small, medium, large]")
        except Exception as e:
            logging.exception("Order volume did not create because %s" % e)

    @property
    def volume(self):
        return self.__volume

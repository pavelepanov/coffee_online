import logging
from decimal import Decimal

from coffee_online.domain.common.errors import ValueObjectValidationError
from coffee_online.domain.common.value_object import ValueObject

logger = logging.getLogger(__name__)


class CoffeeCost(ValueObject):
    def __init__(self, cost: Decimal):
        self.__cost = cost
        self._validate()

    def _validate(self) -> None:
        try:
            if not isinstance(self.__cost, int):
                raise ValueObjectValidationError("Coffee cost must be a decimal")
        except Exception as e:
            logging.exception("Coffee cost did not create because %s" % e)

    @property
    def cost(self):
        return self.__cost

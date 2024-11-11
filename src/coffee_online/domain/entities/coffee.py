from decimal import Decimal

from coffee_online.domain.common.entity import Entity
from coffee_online.domain.value_objects.coffee_cost import CoffeeCost
from coffee_online.domain.value_objects.coffee_description import \
    CoffeeDescription
from coffee_online.domain.value_objects.coffee_id import CoffeeId
from coffee_online.domain.value_objects.coffee_title import CoffeeTitle


class Coffee(Entity):
    def __init__(self, id: CoffeeId, title: CoffeeTitle, description: CoffeeDescription, cost: CoffeeCost) -> None:
        super().__init__(id=id)
        self.title = title
        self.description = description
        self.cost = cost


def address_factory(id: int, title: str, description: str, cost: Decimal) -> Coffee:
    return Coffee(
        id=CoffeeId(id),
        title=CoffeeTitle(title),
        description=CoffeeDescription(description),
        cost=CoffeeCost(cost),
    )

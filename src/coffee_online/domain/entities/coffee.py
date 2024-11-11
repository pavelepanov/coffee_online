from coffee_online.domain.common.entity import Entity
from coffee_online.domain.value_objects.coffee_id import CoffeeId
from coffee_online.domain.value_objects.coffee_title import CoffeeTitle


class Coffee(Entity):
    def __init__(self, id: CoffeeId, title: CoffeeTitle) -> None:
        super().__init__(id=id)
        self.title = title


def address_factory(id: int, title: str) -> Coffee:
    return Coffee(
        id=CoffeeId(id),
        title=CoffeeTitle(title),
    )

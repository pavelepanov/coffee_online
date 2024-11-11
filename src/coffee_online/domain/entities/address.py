from coffee_online.domain.common.entity import Entity
from coffee_online.domain.value_objects.address_id import AddressId
from coffee_online.domain.value_objects.address_title import AddressTitle


class Address(Entity):
    def __init__(self, id: AddressId, title: AddressTitle) -> None:
        super().__init__(id=id)
        self.title = title


def coffee_factory(id: int, title: str) -> Address:
    return Address(
        id=AddressId(id),
        title=AddressTitle(title),
    )

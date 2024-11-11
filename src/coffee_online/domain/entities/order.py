from coffee_online.domain.common.entity import Entity
from coffee_online.domain.value_objects.additive_id import AdditiveId
from coffee_online.domain.value_objects.address_id import AddressId
from coffee_online.domain.value_objects.after_time import AfterTime
from coffee_online.domain.value_objects.coffee_id import CoffeeId
from coffee_online.domain.value_objects.order_id import OrderId
from coffee_online.domain.value_objects.user_id import UserId


class Order(Entity):
    def __init__(self,
                 id: OrderId,
                 address_id: AddressId,
                 coffee_id: CoffeeId,
                 additive_id: AdditiveId,
                 after_time: AfterTime,
                 user_id: UserId
):
        super().__init__(id=id)
        self.address_id = address_id
        self.coffee_id = coffee_id
        self.additive_id = additive_id
        self.after_time = after_time
        self.user_id = user_id


def order_factory(
        id: int,
        address_id: int,
        coffee_id: int,
        additive_id: int,
        after_time: int,
        user_id: int
) -> Order:
    return Order(
        id=OrderId(id),
        address_id=AddressId(address_id),
        coffee_id=CoffeeId(coffee_id),
        additive_id=AdditiveId(additive_id),
        after_time=AfterTime(after_time),
        user_id=UserId(user_id),
    )

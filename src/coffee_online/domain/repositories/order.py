from typing import Protocol

from coffee_online.domain.value_objects.additive_id import AdditiveId
from coffee_online.domain.value_objects.address_id import AddressId
from coffee_online.domain.value_objects.after_time import AfterTime
from coffee_online.domain.value_objects.coffee_id import CoffeeId
from coffee_online.domain.value_objects.order_volume import OrderVolume
from coffee_online.domain.value_objects.user_id import UserId


class OrderRepository(Protocol):
    async def create(self,
                     address_id: AddressId,
                     coffee_id: CoffeeId,
                     additive_id: AdditiveId,
                     after_time: AfterTime,
                     user_id: UserId,
                     volume: OrderVolume,
                     ):
        raise NotImplementedError

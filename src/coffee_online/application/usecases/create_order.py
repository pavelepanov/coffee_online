import logging

from coffee_online.application.contracts.orders.requests import \
    CreateOrderRequest
from coffee_online.application.contracts.orders.responses import OrderResponse
from coffee_online.application.protocols.interactor import Interactor
from coffee_online.domain.repositories.order import OrderRepository
from coffee_online.domain.value_objects.additive_id import AdditiveId
from coffee_online.domain.value_objects.address_id import AddressId
from coffee_online.domain.value_objects.after_time import AfterTime
from coffee_online.domain.value_objects.coffee_id import CoffeeId
from coffee_online.domain.value_objects.order_volume import OrderVolume
from coffee_online.domain.value_objects.user_id import UserId

logger = logging.getLogger(__name__)


class CreateOrder(Interactor[CreateOrderRequest, OrderResponse]):
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    async def __call__(self, request: CreateOrderRequest) -> OrderResponse:
        order = await self.order_repository.create(
            address_id=AddressId(request.address_id),
            coffee_id=CoffeeId(request.coffee_id),
            additive_id=AdditiveId(request.additive_id),
            after_time=AfterTime(request.after_time),
            user_id=UserId(request.user_id),
            volume=OrderVolume(request.volume),
        )

        logging.info("Create order")

        return OrderResponse(
            id=order.id.id,
            address_id=order.address_id.address_id,
            coffee_id=order.coffee_id.coffee_id,
            additive_id=order.additive_id.additive_id,
            after_time=order.after_time.after_time,
            user_id=order.user_id.user_id,
            volume=order.volume.volume,
        )

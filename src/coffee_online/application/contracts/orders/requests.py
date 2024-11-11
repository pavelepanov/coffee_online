from dataclasses import dataclass


@dataclass(frozen=True)
class CreateOrderRequest:
    address_id: int
    coffee_id: int
    additive_id: int
    after_time: int
    volume: str
    user_id: int

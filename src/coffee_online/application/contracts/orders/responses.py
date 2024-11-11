from dataclasses import dataclass


@dataclass(frozen=True)
class OrderResponse:
    id: int
    address_id: int
    coffee_id: int
    additive_id: int
    after_time: int
    user_id: int
    volume: str

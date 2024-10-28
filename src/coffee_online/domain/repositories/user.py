from typing import Protocol

from coffee_online.domain.entities.user import User
from coffee_online.domain.value_objects.user_id import UserId


class UserRepository(Protocol):
    async def get_by_id(self, user_id: UserId) -> User:
        raise NotImplementedError

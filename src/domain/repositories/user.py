from typing import Protocol

from src.domain.entities.user import User
from src.domain.value_objects.user_id import UserId


class UserRepository(Protocol):
    async def get_by_id(self, user_id: UserId) -> User:
        raise NotImplementedError
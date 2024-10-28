from coffee_online.domain.common.entity import Entity
from coffee_online.domain.value_objects.user_email import UserEmail
from coffee_online.domain.value_objects.user_hashed_password import \
    UserHashedPassword
from coffee_online.domain.value_objects.user_id import UserId


class User(Entity):
    def __init__(
        self,
        id: UserId,
        email: UserEmail,
        hashed_password: UserHashedPassword,
    ) -> None:
        super().__init__(id=id)
        self.email = email
        self.hashed_password = hashed_password


def user_factory(
    id: int, email: str, hashed_password: str
) -> User:
    return User(
        id=UserId(id=id),
        email=UserEmail(email=email),
        hashed_password=UserHashedPassword(hashed_password=hashed_password),
    )

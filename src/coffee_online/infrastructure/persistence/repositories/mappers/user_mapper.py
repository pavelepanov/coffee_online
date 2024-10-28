from coffee_online.domain.entities.user import User
from coffee_online.domain.value_objects.user_email import UserEmail
from coffee_online.domain.value_objects.user_hashed_password import \
    UserHashedPassword
from coffee_online.domain.value_objects.user_id import UserId
from coffee_online.infrastructure.persistence.models.user import UserDb


def user_from_db_to_entity(user: UserDb) -> User:
    return User(
        id=UserId(user.id),
        email=UserEmail(user.email),
        hashed_password=UserHashedPassword(user.hashed_password),
    )

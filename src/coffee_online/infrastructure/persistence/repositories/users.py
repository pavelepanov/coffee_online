import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from coffee_online.domain.entities.user import User
from coffee_online.domain.repositories.user import UserRepository
from coffee_online.domain.value_objects.user_id import UserId
from coffee_online.infrastructure.persistence.models.user import UserDb
from coffee_online.infrastructure.persistence.repositories.mappers.user_mapper import \
    user_from_db_to_entity

logger = logging.getLogger(__name__)


class SqlalchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, user_id: UserId) -> User:
        try:
            query = select(UserDb).where(UserDb.id == user_id.id)
            result = await self.session.execute(query)

            logging.info("Selected user by id")

            user: UserDb = result.scalar()

            logging.info("Return user by id after select")

            return user_from_db_to_entity(user)
        except Exception as e:
            logging.exception("User did not selected because %s" % e)

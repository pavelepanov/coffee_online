import logging

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from coffee_online.domain.entities.profile import Profile, profile_factory
from coffee_online.domain.repositories.profile import ProfileRepository
from coffee_online.domain.value_objects.profile_name import ProfileName
from coffee_online.domain.value_objects.profile_sex import ProfileSex
from coffee_online.domain.value_objects.user_id import UserId
from coffee_online.infrastructure.persistence.models.profile import ProfileDb

logger = logging.getLogger(__name__)

class SqlalchemyProfileRepository(ProfileRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(
        self, name: ProfileName, sex: ProfileSex, user_id: UserId
    ) -> Profile:
        stmt = (
            insert(ProfileDb)
            .values(
                name=name.name,
                sex=sex.sex,
                user_id=user_id.id,
            )
            .returning(
                ProfileDb.id,
                ProfileDb.name,
                ProfileDb.sex,
                ProfileDb.user_id,
            )
        )

        result = await self.session.execute(stmt)
        await self.session.commit()

        logging.info('Commit Profile')

        profile = result.mappings().first()

        logging.info('Return Profile after commit')
        return profile_factory(
            id=profile.id,
            name=profile.name,
            sex=profile.sex,
            user_id=profile.user_id,
        )

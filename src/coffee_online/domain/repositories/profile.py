from typing import Protocol

from coffee_online.domain.entities.profile import Profile
from coffee_online.domain.value_objects.profile_name import ProfileName
from coffee_online.domain.value_objects.profile_sex import ProfileSex
from coffee_online.domain.value_objects.user_id import UserId


class ProfileRepository(Protocol):
    async def create(
        self, name: ProfileName, sex: ProfileSex, user_id: UserId
    ) -> Profile:
        raise NotImplementedError

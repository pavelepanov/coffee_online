
from coffee_online.domain.common.entity import Entity
from coffee_online.domain.value_objects.profile_id import ProfileId
from coffee_online.domain.value_objects.profile_name import ProfileName
from coffee_online.domain.value_objects.profile_sex import ProfileSex
from coffee_online.domain.value_objects.user_id import UserId


class Profile(Entity):
    def __init__(self, id: ProfileId, name: ProfileName, sex: ProfileSex, user_id: UserId) -> None:
        super().__init__(id=id)
        self.name = name
        self.sex = sex
        self.user_id = user_id


def profile_factory(
    id: int,
    name: str,
    sex: str,
    user_id: int,
) -> Profile:
    return Profile(
            id=ProfileId(id=id),
            name=ProfileName(name=name),
            sex=ProfileSex(sex=sex),
            user_id=UserId(id=user_id),
        )

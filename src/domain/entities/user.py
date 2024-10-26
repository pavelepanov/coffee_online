from src.domain.common.entity import Entity
from src.domain.value_objects.user_email import UserEmail
from src.domain.value_objects.user_hashed_password import UserHashedPassword
from src.domain.value_objects.user_id import UserId



from src.domain.value_objects.user_name import UserName
from src.domain.value_objects.user_sex import UserSex


class User(Entity):
    def __init__(self, id: UserId, name: UserName, sex: UserSex, email: UserEmail, hashed_password: UserHashedPassword) -> None:
        super().__init__(id=id)
        self.name = name
        self.sex = sex
        self.email = email
        self.hashed_password = hashed_password


def user_factory(
        id: int,
        name: str,
        sex: str,
        email: str,
        hashed_password: str
) -> User:
    return User(
        id=UserId(id=id),
        name=UserName(name=name),
        sex=UserSex(sex=sex),
        email=UserEmail(email=email),
        hashed_password=UserHashedPassword(hashed_password=hashed_password),
    )

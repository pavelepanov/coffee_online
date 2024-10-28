from coffee_online.application.contracts.users.requests import \
    GetUserByIdRequest
from coffee_online.application.contracts.users.responses import UserResponse
from coffee_online.application.protocols.interactor import Interactor
from coffee_online.domain.repositories.user import UserRepository
from coffee_online.domain.value_objects.user_id import UserId


class GetUserById(Interactor[GetUserByIdRequest, UserResponse]):
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(self, request: GetUserByIdRequest) -> UserResponse:
        user = await self.user_repository.get_by_id(user_id=UserId(request.id))

        return UserResponse(
            id=user.id.id,
            email=user.email.email,
            hashed_password=user.hashed_password.hashed_password,
        )

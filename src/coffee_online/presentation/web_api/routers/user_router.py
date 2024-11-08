import logging

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from coffee_online.application.contracts.users.requests import \
    GetUserByIdRequest
from coffee_online.application.contracts.users.responses import UserResponse
from coffee_online.application.usecases.get_user_by_id import GetUserById

user_router = APIRouter(tags=["user"], route_class=DishkaRoute)

logger = logging.getLogger(__name__)


@user_router.get(
    "/user/{user_id}",
    response_model=UserResponse,
    description="Get user by id",
)
async def create_user(
    user_id: int, interactor: FromDishka[GetUserById]
) -> UserResponse:
    logging.info('GET /user/{user_id}')
    return await interactor(
        GetUserByIdRequest(
            id=user_id,
        )
    )

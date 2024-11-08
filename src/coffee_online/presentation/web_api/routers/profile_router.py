import logging

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from coffee_online.application.contracts.profiles.requests import \
    CreateProfileRequest
from coffee_online.application.contracts.profiles.responses import \
    ProfileResponse
from coffee_online.application.usecases.create_profile import CreateProfile
from coffee_online.presentation.web_api.schemas.profiles import \
    ProfileCreateSchema

logger = logging.getLogger(__name__)

profile_router = APIRouter(tags=["profile"], route_class=DishkaRoute)


@profile_router.post(
    "/profile", response_model=ProfileResponse, description="Create profile"
)
async def create_profile(
    schema: ProfileCreateSchema, interactor: FromDishka[CreateProfile]
) -> ProfileResponse:
    logging.info('POST /profile')
    return await interactor(
            CreateProfileRequest(
                name=schema.name,
                sex=schema.sex,
                user_id=schema.user_id,
            )
        )

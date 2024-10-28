from coffee_online.application.contracts.profiles.requests import \
    CreateProfileRequest
from coffee_online.application.contracts.profiles.responses import \
    ProfileResponse
from coffee_online.application.protocols.interactor import Interactor
from coffee_online.domain.repositories.profile import ProfileRepository
from coffee_online.domain.value_objects.profile_name import ProfileName
from coffee_online.domain.value_objects.profile_sex import ProfileSex
from coffee_online.domain.value_objects.user_id import UserId


class CreateProfile(Interactor[CreateProfileRequest, ProfileResponse]):
    def __init__(self, profile_repository: ProfileRepository) -> None:
        self.profile_repository = profile_repository

    async def __call__(self, request: CreateProfileRequest) -> ProfileResponse:
        profile = await self.profile_repository.create(
            name=ProfileName(request.name),
            sex=ProfileSex(request.sex),
            user_id=UserId(request.user_id),
        )

        return ProfileResponse(
            id=profile.id.id,
            name=profile.name.name,
            sex=profile.sex.sex,
            user_id=profile.user_id.id,
        )

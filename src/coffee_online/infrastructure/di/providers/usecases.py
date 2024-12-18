from dishka import Provider, Scope, provide

from coffee_online.application.usecases.create_profile import CreateProfile
from coffee_online.application.usecases.get_user_by_id import GetUserById


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    get_user_by_id = provide(GetUserById)
    profile_create = provide(CreateProfile)

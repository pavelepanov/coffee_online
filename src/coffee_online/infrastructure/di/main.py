from dishka import AsyncContainer, make_async_container

from coffee_online.infrastructure.di.providers.adapters import (
    FastapiUsersProvider, SqlalchemyProvider)
from coffee_online.infrastructure.di.providers.usecases import UseCasesProvider


def container_factory() -> AsyncContainer:
    return make_async_container(
        SqlalchemyProvider(), UseCasesProvider(), FastapiUsersProvider()
    )

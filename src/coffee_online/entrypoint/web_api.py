from logging import DEBUG, FileHandler, StreamHandler, basicConfig

from dishka.integrations.fastapi import FromDishka, setup_dishka
from fastapi import FastAPI

from coffee_online.infrastructure.auth.manager import (auth_backend,
                                                       fastapi_users)
from coffee_online.infrastructure.di.main import container_factory
from coffee_online.presentation.web_api.exc_handlers import \
    init_exception_handlers
from coffee_online.presentation.web_api.routers.profile_router import \
    profile_router
from coffee_online.presentation.web_api.routers.user_router import user_router
from coffee_online.presentation.web_api.schemas.auth import (UserCreate,
                                                             UserRead)


def configure_logging(level=DEBUG):
    format = '[%(asctime)s.%(msecs)03d] %(module)15s:%(lineno)-3d %(levelname)-7s - %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'

    file_handler = FileHandler('logs.log')
    file_handler.setLevel(level)

    console_handler = StreamHandler()
    console_handler.setLevel(level)

    basicConfig(
        level=level,
        datefmt=datefmt,
        format=format,
        handlers=[file_handler, console_handler]
                        )


def init_di(app: FastAPI) -> None:
    setup_dishka(container_factory(), app)


def init_routers(app: FastAPI) -> None:
    app.include_router(
        fastapi_users.get_auth_router(FromDishka[auth_backend]),
        prefix="/auth/jwt",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["auth"],
    )

    app.include_router(user_router)
    app.include_router(profile_router)


def create_app() -> FastAPI:
    app = FastAPI()

    configure_logging()
    init_di(app)
    init_routers(app)
    init_exception_handlers(app)

    return app

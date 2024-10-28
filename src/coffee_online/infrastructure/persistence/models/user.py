from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from coffee_online.infrastructure.persistence.models.base import BaseDb
from coffee_online.infrastructure.persistence.models.types.created_at import \
    created_at
from coffee_online.infrastructure.persistence.models.types.int_pk import intpk
from coffee_online.infrastructure.persistence.models.types.updated_at import \
    updated_at


class UserDb(SQLAlchemyBaseUserTable[int], BaseDb):
    __tablename__ = "user"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String, nullable=False)
    sex: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(
        String, unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
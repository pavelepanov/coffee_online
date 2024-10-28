import datetime
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import mapped_column

updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.now(datetime.UTC),
    ),
]

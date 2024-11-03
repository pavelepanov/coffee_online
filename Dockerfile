FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


WORKDIR /coffee_online

COPY requirements.txt pyproject.toml /coffee_online/

COPY conf /coffee_online/conf
COPY src /coffee_online/src
COPY scripts /coffee_online/scripts
COPY alembic.ini /coffee_online

RUN --mount=type=cache,target=/root/.cache/pip \
    uv pip install -e . --system

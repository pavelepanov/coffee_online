FROM python:3.12-slim

ENV PYTHONPATH=/coffee_online/src

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /coffee_online

# Install the application dependencies.
WORKDIR /coffee_online
RUN uv pip sync 'requirements.txt' --system
RUN uv pip install -e .

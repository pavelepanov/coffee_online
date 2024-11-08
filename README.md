
# Start up project
1. Create .env in /coffee_online/
````
# Example!


# DB settings
DB_HOST=postgres
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASS=123

DATABASE_URI=postgresql+asyncpg://${DB_USER}:${DB_PASS}@${DB_HOST}:${DB_PORT}/${DB_NAME}

# Fastapi users
SECRET_JWT=FDSJFSKJ!3@!sfhu4823482hfjsdfjksd!FDGfdsf432!83128*&*13fdsg
SECRET_MANAGER=fdgkgi!i45$@tiGFGBXdsagfdg3$@
````
2. Build docker in /example_dishka_fastapiusers/
``docker compose up --build``
3. Check docs in ``localhost:8000/docs``

## Logging
Logs will be in docker container in /coffee_online/ in logs.log

### How create logs?

1. Import logging in module like ```import logging```
2. Create logger like ```logger = logging.getLogger(__name__)```
3. Log debug/info/warning/error/exception/critical like ```logging.info('Some text')```

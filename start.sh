#! /usr/bin/env sh

# Exit immediately if a command fails
set -e
# Exit immediately if a command within a pipeline fails
set -o pipefail

# naive sleep to let postgres load, obviously can be made in single compose with healthcheck https://docs.docker.com/compose/compose-file/05-services/#long-syntax-1
sleep 5

alembic -c /app/alembic.ini upgrade head

python /app/src/init_db.py

python /app/src/start.py

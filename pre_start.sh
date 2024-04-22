#! /usr/bin/env bash

# Let the DB start
python app/app/src/pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python app/app/src/init_db.py
#TODO: dockerigonre... docker setup

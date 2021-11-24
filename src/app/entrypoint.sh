#!/bin/bash
alembic upgrade
export PYTHONPATH="."
python3 ./app/tests/testing_utils/db/testing_db.py

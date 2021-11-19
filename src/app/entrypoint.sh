#!/bin/bash
alembic upgrade
export PYTHONPATH="."
python3 ./app/api/main.py

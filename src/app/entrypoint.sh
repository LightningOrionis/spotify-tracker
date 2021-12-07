#!/bin/bash
alembic upgrade head
export PYTHONPATH="."
python3 ./app/main.py

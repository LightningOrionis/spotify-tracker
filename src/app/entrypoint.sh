#!/bin/bash
alembic upgrade
python3 ./app/api/main.py
#!/bin/bash
alembic stamp head
alembic revision --autogenerate -m "Upgrade database with: $1"
alembic upgrade head
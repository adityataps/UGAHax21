#!/bin/bash

MANAGE=manage.py
TEST_DATA=test_data.json

echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
    sleep 0.1
done
echo "PostgreSQL detected!"

echo "Making database migrations..."
python $MANAGE makemigrations --noinput

echo "Applying database migrations..."
python $MANAGE migrate --noinput

echo "[TEMPORARY] Adding test database data..."
python $MANAGE loaddata $TEST_DATA

echo "Collecting static files..."
python $MANAGE collectstatic --noinput

exec "$@"

#!/bin/sh

trap 'exit' INT TERM
trap 'kill 0' EXIT

echo "Waiting for PostgreSQL..."

while ! nc -z pgdb_tracker 5432; do
  sleep 0.1
done

echo "PostgreSQL is ready."


echo "Updating poetry.."
poetry update

echo "Running migrations with Poetry..."
poetry run python manage.py makemigrations
poetry run python manage.py migrate --noinput
echo "Migrations done."

echo "Starting Django application..."
exec poetry run python manage.py runserver 0.0.0.0:8083
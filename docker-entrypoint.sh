#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python3 manage.py makemigrations users
python3 manage.py migrate

#superuser
python3 manage.py shell < createsuperuser.py

# Start server
echo "Starting server"
gunicorn testtask.wsgi:application --bind 0.0.0.0:8000 --workers 3
FROM python:3.10.6-alpine

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

RUN gunicorn testtask.wsgi:application --bind 0.0.0.0:8000
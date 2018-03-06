#!/usr/bin/env bash

echo "Waiting for postgres..."

while ! nc -z example_news_api_db 3306; do
  sleep 0.1
done

echo "PostgreSQL started"

export FLASK_APP=run.py && flask db init && flask db migrate && flask db upgrade

python run.py
#!/bin/bash

cd /rustdesk-api-server;

echo "Making migrations.."
python manage.py makemigrations
echo "Migrating.."
python manage.py migrate
echo "Starting server.."
python manage.py runserver $HOST:21114;

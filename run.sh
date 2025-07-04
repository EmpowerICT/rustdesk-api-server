#!/bin/bash

cd /rustdesk-api-server;

if [ ! -e "./db/db.sqlite3" ]; then
    cp "./db_bak/db.sqlite3" "./db/db.sqlite3"
    echo "No database present, so copied initial database"
fi

echo "Making migrations.."
python manage.py makemigrations
echo "Migrating.."
python manage.py migrate
echo "Starting server.."
python manage.py runserver $HOST:21114;

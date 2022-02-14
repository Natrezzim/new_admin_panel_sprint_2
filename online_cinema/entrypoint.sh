#!/bin/sh

if [ "$DB_NAME" = "movies_database" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python app/manage.py runserver 0.0.0.0:8000


exec "$@"
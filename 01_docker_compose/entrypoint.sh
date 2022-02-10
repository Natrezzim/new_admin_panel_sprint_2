#!/bin/sh

if [ "$DB_NAME" = "movies_database" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python app/manage.py flush --no-input
python app/manage.py migrate
if [ -d "app/sqlite_to_postgres" ]
then
  python app/sqlite_to_postgres/load_data.py
fi
if [ -d "app/tests/check_consistency" ]
then
  pytest app/tests/check_consistency/test_load_data.py
fi
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME','$DJANGO_SUPERUSER_EMAIL','$DJANGO_SUPERUSER_PASSWORD')" | python app/manage.py shell
rm -rf app/sqlite_to_postgres
rm -rf app/tests
rm -rf app/sqlscript
rm -rf app/movies_schema.sql
python app/manage.py runserver 0.0.0.0:8000


exec "$@"
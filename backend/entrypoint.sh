#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# The db operation to perform...
python src/manage.py db init -d src/migrations  
python src/manage.py db migrate -d src/migrations  
python src/manage.py db upgrade -d src/migrations  

exec "$@"
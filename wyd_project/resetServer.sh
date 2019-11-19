#!/bin/bash
echo "welcome"

shopt -s extglob

rm db.sqlite3

cd event/migrations

rm -v !("__init__.py")

cd ../..

cd rso/migrations

rm -v !("__init__.py")

cd ../..

cd university/migrations

rm -v !("__init__.py")

cd ../..

cd users/migrations

rm -v !("__init__.py")

cd ../..

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser 


python3 manage.py runserver

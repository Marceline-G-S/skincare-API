#!/bin/bash

rm db.sqlite3
rm -rf ./skincareapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations skincareapi
python3 manage.py migrate skincareapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python manage.py loaddata concern
python manage.py loaddata skintype
python manage.py loaddata customer
python manage.py loaddata journal
python manage.py loaddata userconcern
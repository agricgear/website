#!/bin/sh

mkdir run

echo " * sync database"
./env/bin/python manage.py syncdb && ./env/bin/python manage.py migrate && ./env/bin/gunicorn_django -D --pid=run/django.pid  -b 0.0.0.0:8182

echo "====================== agroguia web deployed ========================"


#!/bin/sh

mkdir run

echo " * sync database"
./env/bin/python manage.py syncdb && ./env/bin/python manage.py migrate && ./env/bin/gunicorn_django -D --pid=run/django.pid  -b 0.0.0.0:8182 && ./env/bin/gunicorn_django --settings app.settings_en -D --pid=run/django.en.pid  -b 0.0.0.0:8183 --pythonpath ~/agroguia-website

echo "====================== agroguia web deployed ========================"


#!/bin/sh

kill -9 `cat run/django.pid` || echo "django isn't running"
echo "=================== Agrotrack stopped ===================="

#!/bin/sh

cd tr/ag_tracker && kill -9 `cat run/django.pid` || echo "django isn't running"
echo "=================== Agrotrack stopped ===================="

#!/bin/bash
python manage.py migrate --noinput
gunicorn fooapi.wsgi:application -b :8000

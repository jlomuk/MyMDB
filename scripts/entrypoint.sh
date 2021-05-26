#!/bin/sh

set -e
sleep 20;
python django/manage.py migrate
python django/manage.py collectstatic --clear --no-input
uwsgi --socket=127.0.0.1:8000 --master --enable-threads --module=config.wsgi:application

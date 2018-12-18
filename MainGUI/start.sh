#!/bin/bash


python manage.py collectstatic --noinput

pwd
ls

python manage.py runserver 0.0.0.0:7000
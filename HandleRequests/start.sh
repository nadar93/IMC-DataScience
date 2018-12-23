#!/bin/bash

mv model.pkl api/
ls

python manage.py runserver 0.0.0.0:8000
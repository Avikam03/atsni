#! /bin/bash
source ./env/bin/activate
set -m # Enable Job Control
python manage.py makemigrations
python manage.py migrate
python manage.py tailwind start & python manage.py runserver && fg
which python
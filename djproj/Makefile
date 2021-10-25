#!/bin/bash

create_migration:
	. ../venv/bin/activate && python manage.py makemigrations cats

migrate: create_migration
	. ../venv/bin/activate && python manage.py migrate

createsuperuser:
	. ../venv/bin/activate && python manage.py createsuperuser

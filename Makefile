SHELL := /bin/bash

create_infra: docker-compose.yml Dockerfile
	sudo docker-compose up -d

prepare_virtual_environment:
	pip install virtualenv
	python3 -m venv venv
	source ./venv/bin/activate
	pip install -r requirements.txt

makemigrations: manage.py
	python3 manage.py makemigrations

migrate_db: manage.py	
	sudo docker exec -ti devops_blog_web_1 sh -c "python manage.py migrate"

start_project: create_infra prepare_virtual_environment makemigrations migrate_db

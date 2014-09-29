all: update

.PHONY: setup
setup: create-venv copy-local-settings

.PHONY: create-venv
create-venv:
	virtualenv venv

.PHONY: update
update: del-pyc
	pip install -r requirements.txt
	python manage.py migrate  --noinput

.PHONY: initial
initial: del-pyc
	pip install -r requirements.txt
	python manage.py syncdb

.PHONY: del-pyc
del-pyc:
	find . -name '*.pyc' -delete

.PHONY: run
run:
	python manage.py runserver

.PHONY: serve
serve:
	python manage.py runserver 0.0.0.0:8000

.PHONY: lint
lint:
	flake8 mt_projects --exclude=migrations,settings

.PHONY: test
test:
	python manage.py test

.PHONY: static
static:
	python manage.py collectstatic --noinput --clear

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: all help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# docker
docker-cmd: install-package settings collect-static run-server
docker-uwsgi-cmd: install-mysql install-package collect-static migrate run-uwsgi


# install
settings:
	@pipenv run make settings-internal

settings-internal:
	@cd src && python -m scripts.generate_secret -a default

cert:
	@cd docs/dev/cert \
	&& openssl req -new -newkey rsa:2048 -nodes -keyout dev.key -out dev.csr -subj "/C=KR/ST=Seoul/L=Gang-nam/O=SecureSign Inc/OU=Dev Team/CN=example.com" \
	&& openssl x509 -req -days 3650 -in dev.csr -signkey dev.key -out dev.crt

install-mysql:
	@apt update && apt install -y mysql-server default-libmysqlclient-dev

install-package:
	@pipenv install --dev
	@pipenv update --dev

collect-static:
	@pipenv run python src/manage.py collectstatic --no-input --clear

migrate:
	@pipenv run python src/manage.py migrate

# run
run-server:
	@pipenv run python src/manage.py runserver 0.0.0.0:8000

run-uwsgi:
	@pipenv run uwsgi --ini /htdocs/www/docs/uwsgi/jun2.ini --import infras.crontab

# test
test:
	@pipenv run python src/manage.py test src --noinput

# pre-processing
lint:
	@pipenv run pylint ./src/ --rcfile=.pylintrc
	@pipenv run flake8

# docker
docker-up:
	@docker-compose up

docker-rebuild-up:
	@docker-compose up --force-recreate --build

docker-shell:
	@docker-compose exec jun2 /bin/bash

docker-kill-all:
	@docker ps -a -q | xargs docker rm -f

docker-logs:
	@docker-compose logs -f jun2

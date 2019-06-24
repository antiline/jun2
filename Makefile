.PHONY: all help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# docker
docker-cmd: package-install settings runserver


# install
settings:
	@pipenv run make settings-internal

settings-internal:
	@cd src && python -m scripts.generate_secret -a default

cert:
	@cd docs/dev/cert \
	&& openssl req -new -newkey rsa:2048 -nodes -keyout dev.key -out dev.csr -subj "/C=KR/ST=Seoul/L=Gang-nam/O=SecureSign Inc/OU=Dev Team/CN=example.com" \
	&& openssl x509 -req -days 3650 -in dev.csr -signkey dev.key -out dev.crt

package-install:
	@pipenv install --dev
	@pipenv update --dev

# run
runserver:
	pipenv run python src/manage.py runserver 0.0.0.0:8000


# test
test:
	@pipenv run python src/manage.py test src --noinput


# docker
docker-up:
	@docker-compose up

docker-rebuild-up:
	@docker-compose up --force-recreate --build

docker-kill-all:
	@docker ps -a -q | xargs docker rm -f

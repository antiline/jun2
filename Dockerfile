FROM python:3.6

RUN apt update \
    && apt install -y mysql-server \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install pip --upgrade \
    && pip3 install pipenv

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /htdocs/www
WORKDIR /htdocs/www

EXPOSE 8000

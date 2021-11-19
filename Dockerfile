#syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=dev
ENV MYSQL_HOST=mysqldb
ENV MYSQL_USER=built
ENV MYSQL_PASSWORD=tliub
ENV MYSQL_SA_USER=root
ENV MYSQL_SA_PASSWORD=SierraMikeEcho
ENV MYSQL_DB=built

RUN [ "env"]
RUN [ "alembic", "upgrade", "head"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

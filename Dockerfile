FROM python:3.6-alpine

COPY . ./

RUN apt-get update && apt-get -y install gcc make

COPY ./Makefile /usr/app/Makefile

RUN mkdir /usr/app
WORKDIR /usr/app

COPY . /usr/app

RUN make start

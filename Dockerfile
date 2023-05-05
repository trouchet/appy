FROM node:19-alpine

COPY . ./

RUN apt-get update && apt-get -y install gcc make

COPY ./Makefile /usr/appMakefile

RUN mkdir /usr/app
WORKDIR /usr/app

COPY . /usr/app

RUN make start

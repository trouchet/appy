FROM node:19-alpine

COPY . ./

COPY ./Makefile ./Makefile

RUN mkdir /usr/app
WORKDIR /usr/app

COPY . /usr/app

RUN make start

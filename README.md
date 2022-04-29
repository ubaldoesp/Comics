# Marvel-Comics

## About this app
This app is made with love and a lot of hard work (even if it's only a test)

## Prerequisites
* [Docker](https://docs.docker.com/get-docker/)
You need to install the docker and docker-compose

## How to run


* Windows

1. Extract and go to the main directory
2. Start docker daemon
3. Open a console and type: `docker-compose up`
4. The docker should start to build and create the image

* Linux

1. Extract and go to the main directory
2. Make sure you have `make` installed on your system
3. Open a console and type: `make run`
4. If that doesn't work, just type: `docker-compose up`

## Details
> db

This app uses Mongo as the database

> django & gunicorn

This app uses the powerful django framework for the backend and the gunicorn to handle the requests

> nginx

It includes famous nginx as proxy reverse

## Deploy
Here you can find my rest API:


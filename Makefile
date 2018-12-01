.PHONY: build test

default: build test

build:
	docker build -t islands .

test:
	docker run --rm islands nosetests tests
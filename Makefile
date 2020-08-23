TAG := latest
image_name = gonzalo-portfolio

all: dist

build:
	docker build -t $(image_name):$(TAG) .

dist: build
	mkdir -p dist/
	docker run --rm \
	--volume $(shell pwd)/dist:/opt/dist \
	--user "$(shell id -u):$(shell id -g)" \
	$(image_name):$(TAG)
	cp index.html dist/
	cp js/gon_analytics.js dist/js/
	cp favicon.ico dist/
	cp -r images/ dist/

clean:
	rm -rf dist/*
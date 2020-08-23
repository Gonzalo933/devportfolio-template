TAG := latest
image_name = gonzalo-portfolio

all: dist

build:
	docker build -t $(image_name):$(TAG) .

dist: build
	mkdir -p dist/
	docker run --rm \
	--volume $(shell pwd)/dist:/opt/dist \
	$(image_name):$(TAG)
	cp index.html dist/
	cp favicon.ico dist/
	cp -r images/ dist/

clean:
	sudo rm -rf dist/*
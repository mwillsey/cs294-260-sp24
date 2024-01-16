.PHONY: all clean build serve deploy

# the :z is necessary on SELinux systems like Fedora
# CONTAINER = podman run --network slirp4netns:port_handler=slirp4netns -it --rm -v "${PWD}":/usr/src/app:z -p "${PORT}:${PORT}" starefossen/github-pages
CONTAINER = podman run --network=host -it --rm -v "${PWD}":/usr/src/app:Z -p "${PORT}:${PORT}" starefossen/github-pages

PORT ?= 4000
JEKYLL ?= ${CONTAINER} jekyll

build:
	$(JEKYLL) build

serve:
	$(JEKYLL) serve --livereload --port $(PORT)

clean:
	rm -rf _site/

deploy: build
	rsync -avz --delete _site/ cs294-260:~/public_html/sp24/

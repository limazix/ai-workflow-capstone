SHELL:=/bin/bash

MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT_DIR := $(dir $(MAKEFILE_PATH))

IMAGE_NAME=ai-capstone
CONTAINER_RUNNER=podman

PYTHON_TOOLS=app
PYTHON_TESTS=tests
PYTHON_SCRIPTS=$(PYTHON_TOOLS) $(PYTHON_TESTS)

init-venv:
	@python -m venv $(ROOT_DIR)/.venv

init: init-venv install

activate:
	@source $(ROOT_DIR)/.venv/bin/activate

install-prod: activate
	@pip install -r requirements.txt

install-dev: activate
	@pip install -r requirements-dev.txt

install: install-dev install-prod

clean: activate
	@rm -r $(ROOT_DIR)/.venv

lint: activate
	@black $(PYTHON_SCRIPTS) --check
	@flake8 $(PYTHON_SCRIPTS) --statistics

test: activate
	@pytest

test-watch: activate
	@pytest -f

coverage: activate
	@pytest --cov=$(PYTHON_TOOLS)

commit:
	git add --interactive
	cz commit

build-api:
	@podman build -t $(IMAGE_NAME) .

serve:
	@podman run -it --rm -p 8080:8080 \
		-v $(ROOT_DIR)/data/:/app/data \
		-v $(ROOT_DIR)/build/:/app/build \
		--security-opt label=desable \
		$(IMAGE_NAME)
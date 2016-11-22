default:

testall: lint test

test:
	python tests.py

lint: flake8 check-manifest

flake8:
	flake8

check-manifest:
	check-manifest

update:
	pip install -r requirements_dev.txt

.PHONY: default testall test lint flake8 check_manifest update

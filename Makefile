.PHONY: develop
develop:
	pip install -e '.[dev]'

.PHONY: test-local
test-local:
	python -m pytest --skip_internet_tests

.PHONY: test
test:
	coverage run -m --source='edenai' py.test
	coverage report


.PHONY: docs
docs:
	cd docs && make html

.PHONY: clean
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -f
	rm -Rf dist
	rm -Rf *.egg-info

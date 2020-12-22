SRC_CORE=fastvector
SRC_TEST=tests
SRC_DOC=docs
SRC_BENCH=benchmarks

ifeq ($(OS), Windows_NT)
	PYTHON=python
	PIP=pip
else
	PYTHON=python3
	PIP=pip3
endif

help:
	@echo "Some available commands:"
	@echo " * tests              - Run unit tests."
	@echo " * test-coverage      - Run unit tests and test coverage."
	@echo " * test-coverage-html - Run unit tests and test coverage (html)."
	@echo " * benchmark          - Run bechmark tests."

test:
	@$(PYTHON) -m pytest $(SRC_TEST)

test-coverage:
	@$(PYTHON) -m pytest --cov=$(SRC_CORE) $(SRC_TEST)
	@$(PYTHON) -m codecov

test-coverage-html:
	@$(PYTHON) -m pytest --cov=$(SRC_CORE) $(SRC_TEST) --cov-report=html

benchmark:
	@$(PYTHON) -m py.test --benchmark-columns=mean,stddev,rounds,iterations --benchmark-sort=mean $(SRC_BENCH)

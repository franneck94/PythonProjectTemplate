SRC_CORE=fastvector
SRC_TEST=tests
SRC_BENCHMARK=benchmarks

PYTHON=python
PIP=pip

help:
	@echo "Available Commands:"
	@echo " tests                  - Run unit tests."
	@echo " tests-coverage         - Run unit tests and code coverage."
	@echo " tests-coverage-html    - Run unit tests, code coverage and generate html."
	@echo " benchmark              - Run benchmark tests."

test:
	$(PYTHON) -m pytest $(SRC_TEST)

test-coverage:
	$(PYTHON) -m pytest --cov=$(SRC_CORE) $(SRC_TEST)
	$(PYTHON) -m codecov

test-coverage-html:
	$(PYTHON) -m pytest --cov=$(SRC_CORE) $(SRC_TEST) --cov-report=html

benchmark:
	$(PYTHON) -m py.test --benchmark-columns=min,max,mean,stddev --benchmark-sort=mean $(SRC_BENCH)

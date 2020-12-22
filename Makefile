SRC_CORE=fastvector
SRC_TEST=tests
SRC_DOC=docs
SRC_BENCH=benchmarks

ifeq ($(OS), Windows_NT)
	PYTHON=python
	PIP=pip
	RM=del /Q
	FixPath=$(subst /,\,$1)
	BUILD_DOC=cd $(SRC_DOC) && build_docs.bat
else
	# If you use anaconda, you can set
	# Python=python
	# PIP=pip
	# Otherwise:
	PYTHON=python3
	PIP=pip3
	RM=rm -f
	FixPath=$1
	BUILD_DOC=cd $(SRC_DOC) && ./build_docs.sh
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

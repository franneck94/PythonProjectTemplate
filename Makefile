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
	@echo " * test         		- Run unit tests."
	@echo " * test-coverage  	- Run unit tests and test coverage."
	@echo " * test-coverage-html- Run unit tests and test coverage (html)."
	@echo " * doc          		- Document code (pydoc)."
	@echo " * clean        		- Cleanup (e.g. pyc files)."
	@echo " * code-pylint  		- Check code pylint."
	@echo " * code-mypy    		- Check code mypy"
	@echo " * code-isort   		- Sort the import statements."
	@echo " * code-pep8 		- Auto format the code for pep8."
	@echo " * deps-install 		- Install dependencies (see requirements.txt)."
	@echo " * deps-dev-install 	- Install dev. dependencies (see requirements-dev.txt)."

install:
	@$(PYTHON) setup.py install

test:
	@$(PYTHON) -m pytest $(SRC_TEST)

test-coverage:
	@$(PYTHON) -m pytest --cov=$(SRC_CORE) $(SRC_TEST)
	@$(PYTHON) -m codecov

test-coverage-html:
	@$(PYTHON) -m pytest --cov=$(SRC_CORE) $(SRC_TEST) --cov-report=html

benchmark:
	@$(PYTHON) -m py.test --benchmark-columns=mean,stddev,median,rounds,iterations --benchmark-sort=mean $(SRC_BENCH)

doc:
	@$(BUILD_DOC)

clean:
	@$(RM) $(call FixPath,$(SRC_CORE)/__pycache__)
	@$(RM) $(call FixPath,$(SRC_TEST)/__pycache__)

code-pylint:
	@$(PYTHON) -m pylint $(SRC_CORE)

code-mypy:
	@$(PYTHON) -m mypy $(SRC_CORE)

code-isort:
	@$(PYTHON) -m isort --recursive $(SRC_CORE)

code-pep8:
	@$(PYTHON) -m autopep8 -i -r $(SRC_CORE)

deps-install:
	@$(PIP) install -r requirements.txt

deps-dev-install:
	@$(PIP) install -r requirements-dev.txt

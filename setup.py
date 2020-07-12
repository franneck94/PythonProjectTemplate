# Option 1: python setup.py develop
# Option 2: python setup.py bdist_wheel & pip install ./fastvector-0.1.0-py3-none-any.whl
from setuptools import setup


def get_readme():
    with open('README.md') as f:
        return f.read()

def get_license():
    with open('LICENSE') as f:
        return f.read()

CLASSIFIERS = '''\
License :: OSI Approved
Programming Language :: Python :: 3.7 :: 3.8
Topic :: Software Development
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
'''

DISTNAME = 'fastvector'
AUTHOR = 'Jan Schaffranek'
AUTHOR_EMAIL = 'jan.schaffranek@email.com'
DESCRIPTION = 'This is a simple vector package.'
LICENSE = get_license()
README = get_readme()

MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = True
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

PYTHON_MIN_VERSION = '3.7'
PYTHON_MAX_VERSION = '3.8'
SCIPY_MIN_VERSION = '1.1.0'
NUMPY_MIN_VERSION = '1.14.0'

metadata = dict(
    name=DISTNAME,
    version=VERSION,
    long_description=README,
    packages=['fastvector'],
    python_requires='>={}, <={}'.format(PYTHON_MIN_VERSION, PYTHON_MAX_VERSION),
    install_requires=['numpy>={}'.format(NUMPY_MIN_VERSION),
                      'scipy>={}'.format(SCIPY_MIN_VERSION),],
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    classifiers=[CLASSIFIERS],
    license=LICENSE,
    include_package_data=True
)

def setup_package():
    setup(**metadata)

if __name__ == '__main__':
    setup_package()

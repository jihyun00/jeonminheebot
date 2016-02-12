from setuptools import find_packages, setup

from jeonminheebot import VERSION


install_requires = [
    'flask == 0.10.1',
    'sqlalchemy == 1.0.11',
    'alembic == 0.7.4',
    'flake8 == 2.5.1',
    'html5lib == 0.9999999',
    'lxml == 3.5.0',
    'pync == 1.6.1',
]


tests_require = [
    'pytest >= 2.7.0',
    'httpretty >= 0.8.12',
    'pytest-sugar',
]


def readme():
    with open('README.md') as f:
        try:
            return f.read()
        except (IOError, OSError):
            return None


setup(
    name="jeonminheebot",
    version=VERSION,
    packages=find_packages(),
    url='https://github.com/jihyun00/jeonminheebot',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'tests': tests_require,
    },
    long_description=readme(),
)

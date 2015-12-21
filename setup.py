from setuptools import find_packages, setup

from jeonminheebot import VERSION

install_requires = []


tests_require = [
    'pytest >= 2.7.0',
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
    description='Check python import order.',
    long_description=readme()
)

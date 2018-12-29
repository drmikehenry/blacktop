#!/usr/bin/env python3

from setuptools import setup
import os

NAME = 'blacktop'


def open_file(name):
    return open(os.path.join(os.path.dirname(__file__), name))


__version__ = None


for line in open_file(NAME + '.py'):
    if line.startswith('__version__'):
        exec(line)
        break

setup(
    name=NAME,
    version=__version__,
    py_modules=[NAME],
    install_requires=['black'],
    python_requires='>=3.6',
    license='MIT',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'blacktop=blacktop:main',
        ],
    },
)

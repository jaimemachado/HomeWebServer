#!/usr/bin/env python
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    version='0.1',
    description='HomeNetwork WebServer',
    url='https://github.com/jaimemachado/HomeWebServer',
    author='Jaime Machado',
    license='MIT',
    packages=['homenetwork'],
    install_requires=requirements
)
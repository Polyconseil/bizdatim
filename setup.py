#!/usr/bin/env python

from setuptools import setup

setup(
    name="bizdatim",
    version="0.2.0",
    description="Module for performing simple business day arithmetic; forked from python-bizdatetime",
    license="MIT",
    long_description=open("README.rst").read(),
    author="Sergiy Kuzmenko",
    author_email="sergiy@kuzmenko.org",
    maintainer="Polyconseil Dev Team",
    maintainer_email="opensource+bizdatim@polyconseil.fr",
    url="https://github.com/Polyconseil/bizdatim",
    py_modules=["bizdatim"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

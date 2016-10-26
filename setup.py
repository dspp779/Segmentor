#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='Segmentor',
    description="NAER Segmentor",
    version='1.0',
    author='J.C. Wu, M.H. Bai',
    license='GPLv3',
    url='https://github.com/naernlp/Segmentor',
    packages={'Segmentor'},
    package_dir={'Segmentor': 'Segmentor'},
    package_data={'Segmentor': ['Data/*']},
    scripts=[]
)

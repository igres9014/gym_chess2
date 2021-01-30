# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 20:15:11 2021

@author: JOSEPMARIA
"""

from setuptools import setup, find_packages

setup(
    name = 'gym_chess',
    version = '0.1.0',
    url = '',
    description = '',
    packages = find_packages(),
    install_requires = [
        # Github Private Repository
        #'ExampleRepo @ git+ssh://git@github.com/example_organization/ExampleRepo.git#egg=ExampleRepo-0.1'
        'gym_chess@git+https://github.com/igres9014/gym_chess2.git'
    ]
)

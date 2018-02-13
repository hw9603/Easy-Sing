"""Vocaloid python package configuration."""

from setuptools import setup

setup(
    name='vocaloid',
    version='0.1.0',
    packages=['vocaloid'],
    include_package_data=True,
    install_requires=[
        'pycodestyle==2.3.1',
        'pydocstyle==2.0.0',
        'pylint==1.8.1',
        'pyphen==0.9.4',
        'sh==1.12.14',
        'pygame==1.9.2'
    ],
)

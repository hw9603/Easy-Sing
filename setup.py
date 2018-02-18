"""Vocaloid python package configuration."""

from setuptools import setup

try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {"build_ui": build_ui}
except ImportError:
    cmdclass = {}

setup(
    name='vocaloid',
    version='0.1.0',
    packages=['vocaloid'],
    include_package_data=True,
    cmdclass=cmdclass,
    install_requires=[
        'pycodestyle==2.3.1',
        'pydocstyle==2.0.0',
        'pylint==1.8.1',
        'pyphen==0.9.4',
        'sh==1.12.14',
        'mido==1.2.8',
        'python-rtmidi==1.1.0',
        'PyQt5==5.10.0'
    ],
)

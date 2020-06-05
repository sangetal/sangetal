from setuptools import setup, find_packages

from sangetal.version import __version__

setup(
    name='sangetal',
    version=__version__,
    description='Analytics platform',
    author='Brian Estrada',
    author_email='brianseg014@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sangetal = sangetal.cli:sangetal'
        ]
    }
)
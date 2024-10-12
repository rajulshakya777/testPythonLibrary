# setup.py
from setuptools import setup, find_packages

setup(
    name='hello_world_package',
    version='0.1',
    description='A simple package that prints Hello, World!',
    author='Rajul Shakywar',
    author_email='shakyawar.r@gmail.com',
    packages=find_packages(),
    python_requires='>=3.12',
)

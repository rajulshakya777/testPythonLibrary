# Hello World Package

This package prints "Hello, World!" when the `say_hello` function is called.

## Installation

You can install this package using pip:

```bash
pip install git+https://github.com/yourusername/hello_world_package.git


1. Your directory structure should be like this - 
testPythonLibrary/
├── hello_world_package/
│   ├── __init__.py        # This file can be empty
│   └── hello.py           # This should contain the say_hello function
├── setup.py
└── README.md


Settup file - 
# setup.py
from setuptools import setup, find_packages

setup(
    name='hello_world_package',
    version='0.1',
    description='A simple package that prints Hello, World!',
    author='Rajul Shakywar',
    author_email='shakyawar.r@gmail.com',
    packages=find_packages(),
    python_requires='>=3.10',
)

Main File hello.py function containing the code -

# hello.py
def say_hello():
    print("Hello, World!")

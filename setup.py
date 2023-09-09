#!/usr/bin/env python
from setuptools import setup, find_packages

if __name__ == "__main__":
    long_description = "\n".join([
        open("README.rst").read(),
    ])
    
    setup(
        keywords=['SMS', 'SEND SMS', 'Universal SMS', 'Django SMS'],
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(exclude=['media']) 
    )

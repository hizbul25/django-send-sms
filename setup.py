#!/usr/bin/env python

if __name__ == "__main__":
    import setuptools
    long_description = "\n".join([
        open("README.rst").read(),
    ])
    setuptools.setup(
        keywords=['SMS', 'SEND SMS', 'Universal SMS', 'Django SMS']
    )

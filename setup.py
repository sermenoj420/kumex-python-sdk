#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name='python-kumex',
    version='1.0.7',
    packages=['kumex', 'kumex/baseRequest', 'kumex/marketData', 'kumex/trade', 'kumex/user'],
    license="MIT",
    author='Grape',
    author_email="grape.zhang@kucoin.com",
    url='https://github.com/Kucoin/kumex-python-sdk',
    description="kumex-api-sdk",
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

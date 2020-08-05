# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='cqfd',
    version="1.011",
    packages=find_packages(),
    author="megadose",
    install_requires=["argparse","fake_useragent"],
    description="cqfd is a tool to search skype account from a name",
    long_description="",
    include_package_data=True,
    url='http://github.com/megadose/cqfd',
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)

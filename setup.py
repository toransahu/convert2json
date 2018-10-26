#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-08-07 19:15

"""
setup.py
"""


import setuptools


__version__ = '0.0.2'
__author__ = 'Toran Sahu  <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the AGPL license.'


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="convert2json",
        version="0.0.2",
        author="Toran Sahu",
        author_email="toran.sahu@yahoo.com",
        description="Convert compatible python data types, CSV, XLSX, XLS files to JSON string. ",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/toransahu/convert2json",
        packages=setuptools.find_packages(),
        classifiers=(
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
            "Operating System :: OS Independent",
            'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: System :: Archiving :: Packaging',
            "Topic :: Text Processing",
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Intended Audience :: End Users/Desktop",
            "Intended Audience :: Information Technology",
            "Natural Language :: English",

        ),
        keywords=(
            "list to json",
            "dict to json",
            "string to json",
            "hex to json",
            "excel to json", 
            "xlsx to json", "xls to json", 
            "xlsx", "xls", "json",
        ),
        install_requires=(
            "excel2json-3",
            "xlrd",
            "openpyxl",
            "requests",
        )
            
)

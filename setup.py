#! /usr/bin/env python
from setuptools import setup

if __name__ == "__main__":
    setup(
        name='pubmed_parser',
        version='0.2.1',
        description='A python parser for Pubmed Open-Access Subset and MEDLINE XML repository',
        url='https://github.com/titipata/pubmed_parser',
        download_url='https://github.com/titipata/pubmed_parser.git',
        author='Titipat Achakulvisut',
        author_email='my.titipat@gmail.com',
        license='(c) 2015 - 2019 Titipat Achakulvisut, Daniel E. Acuna',
        install_requires=['lxml', 'unidecode', 'requests'],
        packages=['pubmed_parser'],
        package_data={
            'pubmed_parser.data': ['*.xml.gz', '*.nxml', '*.txt'],
        }
    )

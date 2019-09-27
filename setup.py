#!/usr/bin/env python
from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='django-url-or-relative-url-field',
    version='0.1.2',
    description="""This package provides a Django model field that can store both absolute and relative URLs""",
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Timur Kamanin',
    author_email='tim@timonweb.com',
    url='https://timonweb.com/oss/django-url-or-relative-url-field/',
    packages=[
        'url_or_relative_url_field',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="The MIT License (MIT)",
    zip_safe=False,
    keywords='url field, relative url field',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)

#!/usr/bin/env python

"""The setup script."""
from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='appy',
    author='Bruno Peixoto',
    author_email='brunolnetto@gmail.com',
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An appy on Flask",
    install_requires=[],
    license='MIT license',
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords=['Flask'],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    version='0.2.0',
    zip_safe=False,
)
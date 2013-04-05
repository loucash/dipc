#!/usr/bin/env python
#
# Copyright (c) 2012 Lukasz Biedrycki <lukasz.biedrycki@gmail.com>
#

try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='dipc',
    version='0.4',
    description='Distributed Inter-Process Communication Library implemented in Python and Memcache server',
    long_description='\n' + open('README.rst').read(),
    author='Lukasz Biedrycki',
    author_email='lukasz.biedrycki@gmail.com',
    keywords='distributed ipc python memcache lock semaphore inter process communication',
    license='New BSD License',
    url='https://github.com/loucash/dipc',
    tests_require=['nose', 'mock'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    requires=['python_memcached'],
    install_requires=[
        'python_memcached>=1.48',
    ],
    data_files=[("", ['README.rst'])],
    package_data={'': ['README.rst']},
)

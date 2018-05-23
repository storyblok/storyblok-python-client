import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='storyblok',
    version='0.1.1',
    description='Storyblok API library client for python',
    author='Dominik Angerer',
    author_email='da@storyblok.com',
    url='https://github.com/storyblok/storyblok-python-sdk',
    download_url = 'https://github.com/storyblok/storyblok-python-sdk/archive/0.1.1.tar.gz',
    license='MIT',
    install_requires=[
        'requests >= 2.1.0'
    ],
    packages=[
        'storyblok'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

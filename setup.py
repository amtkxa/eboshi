#!/usr/bin/env python
# encoding: utf-8

from setuptools import find_packages, setup

setup(
    name='eboshi',
    version='0.0.5',
    description='Azkaban CLI tool',
    long_description=open('README.md').read(),
    author='wyukawa',
    author_email='wyukawa@gmail.com',
    url='https://github.com/wyukawa/eboshi',
    license='MIT',
    packages=find_packages(),
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
      'Environment :: Console',
    ],
    install_requires=[
      'requests',
      'cliff'
    ],
    entry_points={
        'console_scripts': [
            'eboshi = eboshi.main:main'
        ],
        'eboshi': [
            'upload = eboshi.upload:Upload',
            'addschedule = eboshi.add_schedule:Add_Schedule',
            'exec = eboshi.exec:Exec',
        ]
    },
)


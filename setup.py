#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Salim Benhamadi",
    author_email='salim.benhamadi@outlook.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="PyEquilibria is a Python package designed for game theory exploration. It provides functionalities to simulate and analyze strategic interactions in games. With PyEquilibria, users can uncover Nash equilibria, optimize strategies, and gain insights into various aspects of game theory. The package aims to be a versatile tool for those interested in understanding and experimenting with strategic decision-making in Python.",
    entry_points={
        'console_scripts': [
            'PyEquilibria=PyEquilibria.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='PyEquilibria',
    name='PyEquilibria',
    packages=find_packages(include=['PyEquilibria', 'PyEquilibria.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/salim-benhamadi/PyEquilibria',
    version='0.1.0',
    zip_safe=False,
)

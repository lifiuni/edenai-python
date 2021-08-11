#!/usr/bin/env python3
"""
edenai-python
"""

import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    raise RuntimeError("edenai-python supports Python 3.6 and above.")

# This import must be below the above `sys.version_info` check,
# because the code being imported here is not compatible with the older
# versions of Python.
from edenai import __version__ as version

INSTALL_REQUIRES = [
    "requests",
]

EXTRAS_DEV_DOCS = [
    "Sphinx",
    "sphinx-rtd-theme>=0.5.2",
    "pytest",
    "coverage",
    "python-dotenv",
]

setup(
    name="edenai",
    version=version,
    description="Eden AI simplifies the use and integration of AI technologies by providing a unique API connected to the best AI engines and combined with a powerful management platform. The platform covers a wide range of AI technologies.",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author="EDENAI",
    author_mail="contact@edenai.co",
    maintainer="samyme",
    maintainer_email="samy@datagenius.fr",
    url="https://github.com/edenai/edenai-python/",
    packages=find_packages(exclude=["*test*"]),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "dev": (EXTRAS_DEV_DOCS,),
    },
    license="",
    keywords="",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)

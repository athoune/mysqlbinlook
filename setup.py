#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="Mysqlbinlook",
      version="0.1",
      description="Reading and parsing mysqlbinlog data",
      license="GPLv3",
      author="Mathieu Lecarme",
      package_dir={'': 'src/'},
      keywords= ["mysql"],
      zip_safe = True,
      #install_requires=[],
      scripts=['bin/mysqlbinlook'])
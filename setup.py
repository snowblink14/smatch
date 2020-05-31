#!/usr/bin/env python

import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as f:
    README = f.read()


setup(name="smatch",
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description="Smatch (semantic match) tool",
      long_description=README,
      long_description_content_type='text/markdown',
      author="Shu Cai",
      author_email="shucai.work@gmail.com",
      url="https://github.com/snowblink14/smatch",
      license="MIT",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing :: Linguistic',
          'Topic :: Utilities'
      ],
      keywords='nlp semantics amr evaluation',
      py_modules=["smatch", "amr"],
      scripts=["smatch.py"],
      )

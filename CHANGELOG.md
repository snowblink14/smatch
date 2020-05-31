
# Changelog

## Unreleased

(no unreleased changes yet)

## [1.0.4]

**Release date: 2020-05-30**

* Python 2 support is removed ([#31])
* Python 3.8 support is added

## [1.0.3]

**Release date: 2020-05-30**

> Note: due to an issue with deployment, this was released as v1.0.3.2

* Smatch version is taken from git tag (see [#22])
* Add CI/CD configuration (see PR [#23])
* Better handle deinversion of special roles ([#10])
* Get `smatch-table.py` working again (part of PR [#27])
* Add `tests/` subdirectory and `test_top.py` ([#25])
* Make TOP relation's value a constant string and not the top node's
  concept to avoid double-penalizing different top concepts ([#25])

## [1.0.2]

**Release date: 2019-12-24**

* Windows support ([#19])

## [1.0.1]

**Release date: 2018-08-21**

* Refactor to allow programmatic usage ([#14])


## [1.0]

**Release date: 2018-08-12**

* Add Smatch to PyPI ([#5])


## Pre-1.0

The following are taken from an old `update_log` file:

* Update: 01/08/2017

  Person involved: Shu Cai

  A bit refactoring and cleanup for easier debugging and better code quality.
  This change does not affect the functionality of smatch.

* Update: 12/18/2016

  Person involved: Shu Cai

  Add an error message for AMR parsing error, and fix a bug introduced
  by a typo in the previous commit.

* Update: 12/14/2016

  Person involved: Shu Cai

  Fix a bug introduced in 11/06/2016: not supporting multiple
  same-name relationships

  Thanks Miguel Ballesteros (miguel.ballesteros@ibm.com) to bring this up.

* Update: 11/14/2016

  Person involved: Jon May

  Fix a bug: quoted and unquoted strings match (propagation of old bug
  to github) Thanks William Dolan

* Update: 11/06/2016

  Person involved: Shu Cai

  Fix a bug: not supporting multiple relationships between two (same) nodes

  Thanks Marco Damonte (s1333293@sms.ed.ac.uk) for finding this bug!

* Update: 1/9/2016

  Person involved: Guntis Barzdins and Didzis Gosko

  Fixed small crash bug

* Update: 12/21/2015

  Person involved: Jon May

  Fixed treatment of quoted strings to allow special characters to be
  actually part of the string.

  Empty double quoted strings also allowed

* Update: 01/18/2015

  Person involved: Shu Cai

  Code cleanup and bug fix. Add detailed comment to the code.

  Thanks Yoav Artzi (yoav@cs.washington.edu) for finding a bug and
  fixing it.

* Update: 04/04/2013

  Person involved: Shu Cai

  Add Software_architecture.pdf. Minor changes to the smatch.py and
  smatch-table.py (comments and add --pr option)

  Minor changes to the README.txt and smatch_guide.pdf

* Update: 03/20/2013

  Person involved: Shu Cai

  Minor changes to the documents: smatch_guide.txt and smatch_guide.pdf

* Update: 03/19/2013

  Person involved: Shu Cai

  Document update. The latest documents are smatch_guide.txt and
  smatch_guide.pdf (same content)

  Add some sample files to the directory: sample_file_list,
  test_input1, test_input2

* Update: 03/17/2013

  Person involved: Shu Cai

  Interface change of smatch.py and smatch-table.py. Using this
  version does not require esem-format-check.pl. (All versions before
  v0.5 require esem-format-check.pl to check the format of AMR)
  Instead it needs amr.py.

  It now accepts one-AMR-per-line format as well as other formats of AMR.

  smatch.py now equals to smatch-v0.5.py
  smatch-table.py now equals to smatch-table-v0.3.py

* Update: 09/14/2012

  Person involved: Shu Cai

  Bug fix of smatch.py and smatch-table.py. smatch-v0.1.py
  smatch-v0.2.py smatch-v0.3.py smatch-v0.4.py smatch-table-v0.1.py
  smatch-table-v0.2.py was created.

  smatch.py now equals to smatch-v0.4.py

  smatch-table.py now equals to smatch-table-v0.2.py

  smatch.py runs with a smart initialization, which matches words with
  the same value first, then randomly select other variable
  mappings. 4 restarts is applied.

* Update: 08/22/2012

  Person involved: Shu Cai

  Minor bug fix of smatch.py. smatch-v2.py was created.

  - smatch.py-> smatch-v1.py
  - smatch-v2.py-> smatch.py

  No change of interface


[1.0.4]: https://pypi.org/project/smatch/1.0.4/
[1.0.3]: https://pypi.org/project/smatch/1.0.3.2/
[1.0.2]: https://pypi.org/project/smatch/1.0.2/
[1.0.1]: https://pypi.org/project/smatch/1.0.1/
[1.0]: https://pypi.org/project/smatch/1.0.post2/

[#5]: https://github.com/snowblink14/smatch/issues/5
[#7]: https://github.com/snowblink14/smatch/issues/7
[#10]: https://github.com/snowblink14/smatch/issues/10
[#14]: https://github.com/snowblink14/smatch/issues/14
[#19]: https://github.com/snowblink14/smatch/issues/19
[#22]: https://github.com/snowblink14/smatch/issues/22
[#23]: https://github.com/snowblink14/smatch/pull/23
[#25]: https://github.com/snowblink14/smatch/pull/25
[#27]: https://github.com/snowblink14/smatch/pull/27
[#31]: https://github.com/snowblink14/smatch/issues/31


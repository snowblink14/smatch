# Smatch (semantic match) tool

[![Version on PyPI](https://img.shields.io/pypi/v/smatch)](https://pypi.org/project/smatch/)
![Python Support](https://img.shields.io/pypi/pyversions/smatch)

[Smatch](http://amr.isi.edu/evaluation.html) is an evaluation tool for
[AMR](http://amr.isi.edu/) (Abstract Meaning Representation). It
computes the Smatch score (defined below) of two AMR graphs in terms
of their matching triples (edges) by finding a variable (node) mapping
that maximizes the count, `M`, of matching triples, then:

* `M` is the number of matching triples
* `T` is the total number of triples in the first AMR
* `G` is the total number of triples in the second AMR
* Precision is defined as `P = M/T`
* Recall is defined as `R = M/G`
* The Smatch score is the F-score: `F = 2 * (P*R)/(P+R)`

For more information, see [Cai and Knight,
2013](https://amr.isi.edu/smatch-13.pdf).

## Requirements, Installation, and Usage

This Smatch implementation is tested for Python 3.5 or higher. It is
released [on PyPI](https://pypi.org/project/smatch/) so you can
install it with `pip`:

``` console
$ pip install smatch
```

You can also clone this repository and run the `smatch.py` script
directly as it does not need to be installed to be used.

To use the script, run it with at least the `-f` option, which takes
two filename arguments:

``` console
$ smatch.py -f test.amr gold.amr
```

Note that the order of these arguments does not matter for the Smatch
score as the F-score is symmetric, but swapping the arguments will
swap the precision and recall. The files contain AMRs separated by a
blank line, with comment lines starting with `#` (see
[`test_input1.txt`](test_input1.txt) for an example).

For other options, try `smatch.py --help`.

## Citation

```bibtex
@inproceedings{cai-knight-2013-smatch,
    title = "{S}match: an Evaluation Metric for Semantic Feature Structures",
    author = "Cai, Shu and Knight, Kevin",
    booktitle = "Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = aug,
    year = "2013",
    address = "Sofia, Bulgaria",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P13-2131",
    pages = "748--752",
}
```

## Recommendations for Reproducible Research

You can help make your research reproducible by including the
following information in your writing:

* The software version (e.g., repository URL and version number)
* The number of restarts (`-r`) used, even if unchanged from the default
* The order of the arguments to `-f` (if reporting precision and recall)
* Any other options or preprocessing steps


## History

The code was mostly developed during 2012 and 2013, and has undergone
many fixes and updates. Note that the versions distributed for
[SemEval-2016](http://alt.qcri.org/semeval2016/task8/index.php?id=data-and-tools)
were numbered 2.0&ndash;2.0.2, but these predate this repository and
the [1.0 series on
PyPI](https://pypi.org/project/smatch/#history). For more details, see
the [Changelog](CHANGELOG.md).


## Related Projects

Here are some notable forks of Smatch:

* [didzis/pSMATCH](https://github.com/didzis/pSMATCH) adds
  parallelization for speed
* [isi-nlp/smatch](https://github.com/isi-nlp/smatch) adds an ILP
  solver for getting optimal variable mappings
* [cfmrp/mtool](https://github.com/cfmrp/mtool) packages the version
  of Smatch used for the [MRP](http://mrp.nlpl.eu/) workshop at [CONLL
  2019](http://www.conll.org/2019)

And here are other evaluation metrics for AMR:

* [mdtux89/amr-evaluation](https://github.com/mdtux89/amr-evaluation)
  offers a set of metrics based on Smatch for fine-grained evaluation
* [freesunshine0316/sembleu](https://github.com/freesunshine0316/sembleu)
  is inspired by BLEU and puts more weight on "content" than
  graph-structure similarity
* [rafaelanchieta/sema](https://github.com/rafaelanchieta/sema/)
  weights error types differently and does not consider which node is
  the graph's top


"""
The top node in an AMR determines the focus of the encoded
meaning. For example, the following have the same dependencies but a
different node at the top:

    (w / white-03
       :ARG1 (m / marble))

The above AMR means "the marble is white" or "the whiteness of the
marble".

    (m / marble
       :ARG1-of (w / white-03))

This AMR means "the marble that is white" or "the white marble".

For this reason, AMRs that differ only in which node is the top will
get smatch scores less than 1.0.

For more information see:

    https://github.com/amrisi/amr-guidelines/blob/master/amr.md#focus
"""

import smatch

a = '(a / alpha :ARG0 (b / beta))'
b = '(a / alternative :ARG0 (b / beta))'
c = '(a / alpha :ARG0 (b / b-side))'
d = '(b / beta :ARG0-of (a / alpha))'


def get_amr_match(amr1, amr2):
    vals = smatch.get_amr_match(amr1, amr2)
    smatch.match_triple_dict.clear()
    return vals


def test_same():
    assert get_amr_match(a, a) == (4, 4, 4)
    smatch.match_triple_dict.clear()


def test_same_top_different_top_concept():
    assert get_amr_match(a, b) == (3, 4, 4)
    smatch.match_triple_dict.clear()


def test_same_top_different_dependent_concept():
    assert get_amr_match(a, c) == (3, 4, 4)
    smatch.match_triple_dict.clear()


def test_same_different_top():
    assert get_amr_match(a, d) == (3, 4, 4)
    smatch.match_triple_dict.clear()

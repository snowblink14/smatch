
# smatch tests

This directory contains test cases to verify the correct behavior of
smatch. Run the tests with [pytest](https://pytest.org/). This will
require you to install both pytest and smatch:

```console
$ pip install pytest
$ pip install -e .  # current directory is smatch
$ pytest
```

**Note:** As smatch is inherently non-deterministic due to its
hill-climbing implementation, the tests can be "flaky" (i.e.,
sometimes pass, sometimes fail). To mitigate the possibility of flaky
tests, test cases should use *minimal* AMRs so it becomes trivial for
smatch to get the optimal solution.

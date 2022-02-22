# types-smorest

This is a package containing type annotations for [flask-smorest](https://pypi.org/project/flask-smorest/).

### Installing:

Simply run the following in the environment in which you want to install this package:

```shell
# install types-smorest
$ python -m pip install types-smorest
```

or add it to your requirements file.

### Developing

This is a partial stub package, only covering a part of the functions and objects available in `flask-smorest`.
Contributions (both in adding stubs for more functions, or keeping up to date with `flask-smorest` itself) are welcome.

All the formatting is done using [pre-commit](https://pre-commit.com/). To use this, run the following:

```shell
# install pre-commit
$ python -m pip install pre-commit

# Set up the hooks (so pre-commit automatically runs when you do a commit)
$ cd root/directory/of/the/pulled/repository
$ pre-commit install

# This will run automatically whenever a commit is created
# To run it manually, use:
$ pre-commit run --all-files
```

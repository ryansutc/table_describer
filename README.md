<h1 align="center">
  <h4 align="center">Data Diff: Compare files with Python</h4>
</h1>

<p align="center">
  <a href="https://travis-ci.org/ryansutc/table_describer">
    <img src="https://travis-ci.org/ryansutc/table_describer.svg?branch=master"
         alt="Build">
  </a>
  <a href="https://raw.githubusercontent.com/ryansutc/table_describer/master/LICENSE">
    <img src="https://img.shields.io/npm/l/express.svg?maxAge=2592000&style=flat-square"
         alt="License">
  </a>
</p>

# table_describer
Quickly get characteristics of a delimited table and its data

table_describer is a small little python package distribution. It contains all of 1 function: `describe_csv(input_table, datefields)`.
It's an experiment and definitely not production-ready; more of a test with building packages in python-land.

## Prerequisites

Requires Python 2x and [pandas python library](https://pandas.pydata.org/)

## Installing from pypi test library

```
pip install  --index-url https://test.pypi.org/simple/ table-describer
```

[todo] is there a way to install this in a project and not machine-wide?

Or install directly from github as a script:
```
pip install git+https://github.com/ryansutc/table_describer.git
```

## Or if you want to pull down to work on and test using a safe python virtual environment:

```
# to install all the python package dependencies:
pipenv install

# to activate the projects virtual env:
pipenv shell

# to run a command inside the virtual env:
pipenv run
```

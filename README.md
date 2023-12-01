### AOC-2023

## Installing

- Required: `Python 3.12.0`

Create a venv:

```
python -m venv aoc-2023
```

Activate the venv (open new terminal, select proper interpreter in vscode) and install

```
pip install setuptools pytest
pip install -e .
```

## Scaffolding

In order to get started on a new day, a scaffolding script is provided. This script will create a dedicated folder for your day, including a python file for the day and a test file for the day. It will also create a `input.txt` file for the day, which can be used to paste the input data for the day.

Scaffolding can be done using the following command:

```
python scaffold.py --day {day}
```

## Running

Any of the part files can be run directly using the built-in vscode runner, or by simply calling the python file e.g;

```
python 01/part1.py
python 01/part2.py
```

The (generated) unit tests can be used to test the test input of the day, just paste the test data in `{day}/test_input.txt` and adjust the expected values in `{day}/day_test.py`.

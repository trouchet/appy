# ![appy_title](https://github.com/trouchet/appy/blob/8c9923dc13b109b83d07a43d6810ebf7b150a2fb/images/appy_small.png)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4e255ae6f2b645fb8f1578a3cc0a2291)](https://www.codacy.com/gh/trouchet/appy/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=trouchet/appy&amp;utm_campaign=Badge_Grade)

An appy on Flask.

## Install
  
Depends on section(s): `[ ]`

Instructions:

- Where: Anywhere on terminal
- What: Run the command below to install `Flask` and `poetry`:

```
apt install python3-flask && curl -sSL https://install.python-poetry.org | python3 -
```

## Setup

Depends on section(s): `[ Install ]`

Instructions:

- Where: On `appy` root path;
- What: Run the commands below:

```
export FLASK_APP="$(pwd)/src/main.py" && poetry shell
```

## Run

Depends on section(s): `[ Install, Setup ]`

Instructions:

- Where: On `appy` root path;
- What: Run the command below:

```
flask run
```

## Lint

Depends on section(s): `[ Install, Setup ]`

Instructions:

- Where: On `appy` root path;
- What: Run the command below:

```
ruff --fix . && pre-commit run --all-files
```

## Test

Depends on section(s): `[ Install, Setup ]`

Instructions:

- Where: On `appy` root path;
- What: Run the command

```
pytest --cov=src
```

## Coverage

Depends on section(s): `[ Install, Setup, Test ]`

Instructions:

- Where: On `appy` root path;
- What: Run the command below:

```
coverage report -m
```

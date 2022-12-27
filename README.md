# ![appy_title](https://github.com/trouchet/appy/blob/8c9923dc13b109b83d07a43d6810ebf7b150a2fb/images/appy_small.png)

An appy on Flask.

## Install

  `apt install python3-flask`

## Run

  `flask --app appy run`

## Debug

  `flask --app appy --debug run`

## Lint

   `ruff --fix . && black . && pre-commit run --all-files`

## Test

  `pytest --cov=src`

## Coverage

  `coverage report -m`

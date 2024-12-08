# Setup
The project is managed using [poetry, the python build & dependency manager](https://python-poetry.org/).

## Setup using poetry
Run `poetry install` to install perfetto.

## Setup using pip
If you do not wish to install poetry on your machine, make sure to `pip install -r requirements.txt`.

# Steps to reproduce
The bug was encountered on an x86_64 Ubuntu 24.04 machine.

1. Make sure that the latest version of vscode is installed;
2. Open the project in vscode: `code perfetto-bug-report`;
3. Open the `Run and Debug` panel in vscode's sidebar, and run the `Reproduce bug` debug configuration.

Just in case you do not run into the bug, the observed exception is stored in the file `error_log.txt`
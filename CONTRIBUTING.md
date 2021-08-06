# Contributing to edenai-python

## Setup
1.  Create a virtualenv
2.  Install `edenai-python` in editable mode along with dev dependencies:

        pip install -e ".[dev]"

## Running tests
To run the full test suite:

    make test

Or simply:

    pytest

To run a specific test module, pass a path as an argument to pytest.
For example:

    pytest test/test_folder/test_module.py
    
    
## Building docs

    make docs

Open `docs/_build/html/index.html` with a browser to see the docs. On macOS you 
can use the following command for that:

    open docs/_build/html/index.html



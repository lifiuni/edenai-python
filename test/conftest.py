#!/usr/bin/env python3

import pytest
import sys

# Create a dict of markers.
# The key is used as option, so --{key} will run all tests marked with key.
# The value must be a dict that specifies:
# 1. 'help': the command line help text
# 2. 'marker-descr': a description of the marker
# 3. 'skip-reason': displayed reason whenever a test with this marker is skipped.
optional_markers = {
    "skip_internet_tests": {
        "help": "Run tests without Internet access",
        "marker-descr": "Skip tests which requires Internet access",
        "skip-reason": "Test only runs without the --skip-internet-tests option.",
    },
}


def pytest_addoption(parser):
    for marker, info in optional_markers.items():
        parser.addoption(
            "--{}".format(marker),
            action="store_false",
            default=True,
            help=info["help"],
        )


def pytest_configure(config):
    for marker, info in optional_markers.items():
        config.addinivalue_line(
            "markers", "{}: {}".format(marker, info["marker-descr"])
        )


def pytest_collection_modifyitems(config, items):
    for marker, info in optional_markers.items():
        print(30 * ">")
        print(config.getoption("--{}".format(marker)))
        print(30 * "<")
        if not config.getoption("--{}".format(marker)):
            skip_test = pytest.mark.skip(reason=info["skip-reason"].format(marker))
            print(30 * ">")
            print(skip_test)
            print(30 * "<")
            for item in items:
                if marker in item.keywords:
                    item.add_marker(skip_test)

#!/usr/bin/env python3
"""Tests for Translation API"""
from test.api.utils import get_api_key

import pytest
from edenai import Translation


@pytest.fixture
def api():
    return Translation(get_api_key())


@pytest.fixture
def api_wrong():
    return Translation("123")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "translation",
            "https://api.edenai.run/v1/pretrained/text/automatic_translation",
        ),
        (
            "language_detection",
            "https://api.edenai.run/v1/pretrained/text/language_detection",
        ),
    ],
)
def test_endpoints(api: Translation, test_input, expected):
    assert api.get_endpoint_url(test_input) == expected

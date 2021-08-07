#!/usr/bin/env python3
"""Tests for Text API"""

import pytest

from edenai import Text


@pytest.fixture
def api():
    # TODO get API key from .env
    return Text("123")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("ner", "https://api.edenai.run/v1/pretrained/text/named_entity_recognition"),
        (
            "sentiment_analysys",
            "https://api.edenai.run/v1/pretrained/text/sentiment_analysis",
        ),
        (
            "syntax_analysis",
            "https://api.edenai.run/v1/pretrained/text/syntax_analysis",
        ),
        (
            "keyword_extraction",
            "https://api.edenai.run/v1/pretrained/text/keyword_extraction",
        ),
    ],
)
def test_endpoints(api: Text, test_input, expected):
    assert api.get_endpoint_url(test_input) == expected

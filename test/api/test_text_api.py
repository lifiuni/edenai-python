#!/usr/bin/env python3
"""Tests for Text API"""

import pytest

from edenai import Text


@pytest.fixture
def api():
    # TODO get API key from .env
    return Text("123")


def test_endpoints(api: Text):
    assert (
        api.get_endpoint_url("ner")
        == "https://api.edenai.run/v1/pretrained/text/named_entity_recognition"
    )
    assert (
        api.get_endpoint_url("sentiment_analysys")
        == "https://api.edenai.run/v1/pretrained/text/sentiment_analysis"
    )
    assert (
        api.get_endpoint_url("syntax_analysis")
        == "https://api.edenai.run/v1/pretrained/text/syntax_analysis"
    )
    assert (
        api.get_endpoint_url("keyword_extraction")
        == "https://api.edenai.run/v1/pretrained/text/keyword_extraction"
    )

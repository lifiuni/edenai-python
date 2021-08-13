#!/usr/bin/env python3
"""Tests for Text API"""

from test.api.utils import get_api_key

import pytest
from edenai import Text


@pytest.fixture
def api():
    return Text(get_api_key())


@pytest.fixture
def api_wrong():
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


@pytest.mark.skip_internet_tests
def test_ner(api: Text):
    result = api.ner(
        providers=["amazon", "ibm"],
        text="I am angry today and will angry tomorrow, and also on the next week",
        language="en-US",
    )

    assert len(result["Amazon Web Services"][0]) > 0
    assert len(result["Amazon Web Services"][1]) > 0


@pytest.mark.skip_internet_tests
def test_sentiment_analysys(api: Text):
    result = api.sentiment_analysys(
        providers=["amazon", "ibm"],
        text="I am angry today and will angry tomorrow, and also on the next week",
        language="en-US",
    )

    assert len(result["Amazon Web Services"][0]) > 0
    assert len(result["Amazon Web Services"][1]) > 0


@pytest.mark.skip_internet_tests
def test_syntax_analysys(api: Text):
    result = api.syntax_analysys(
        providers=["amazon", "ibm"],
        text="I am angry today and will angry tomorrow, and also on the next week",
        language="en-US",
    )

    assert len(result["Amazon Web Services"]) > 0


@pytest.mark.skip_internet_tests
def test_keyword_extraction(api: Text):
    result = api.keyword_extraction(
        providers=["amazon", "ibm"],
        text="I am angry today and will angry tomorrow, and also on the next week",
        language="en-US",
    )

    assert len(result["Amazon Web Services"][0]) > 0
    assert len(result["Amazon Web Services"][1]) > 0


@pytest.mark.skip_internet_tests
def test_ner_error(api_wrong: Text):
    result = api_wrong.ner(
        providers=["amazon", "ibm"],
        text="I am angry today and will angry tomorrow, and also on the next week",
        language="en-US",
    )

    assert "errors" in result


@pytest.mark.skip_internet_tests
def test_sentiment_analysys_error(api_wrong: Text):
    result = api_wrong.sentiment_analysys(
        providers=["amazon", "ibm"],
        text="I am angry today and will angry tomorrow, and also on the next week",
        language="en-US",
    )
    assert "errors" in result


@pytest.mark.skip_internet_tests
def test_syntax_analysys_error(api_wrong: Text):
    result = api_wrong.syntax_analysys(
        providers=["amazon", "ibm"],
        text="I am angry today and will angry tomorrow, and also on the next week",
        language="en-US",
    )
    assert "errors" in result


@pytest.mark.skip_internet_tests
def test_keyword_extraction_error(api_wrong: Text):
    result = api_wrong.keyword_extraction(
        providers=["amazon", "ibm"],
        text="I am angry today and will angry tomorrow, and also on the next week",
        language="en-US",
    )
    assert "errors" in result

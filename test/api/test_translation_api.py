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


@pytest.mark.skip_internet_tests
def test_translation(api: Translation):
    result = api.translation("Text to translate", "en-US", "fr-FR", ["amazon"])

    assert len(result["Amazon Web Services"]) > 0
    assert isinstance(result["Amazon Web Services"], str)


@pytest.mark.skip_internet_tests
def test_language_detection(api: Translation):
    result = api.language_detection("Text to detection", "en", ["amazon"])

    assert len(result["Amazon Web Services"][0]) > 0
    assert len(result["Amazon Web Services"][1]) > 0


@pytest.mark.skip_internet_tests
def test_translation_error(api_wrong: Translation):
    result = api_wrong.translation("Text to translate", "en", "fr", ["amazon"])
    assert "errors" in result


@pytest.mark.skip_internet_tests
def test_language_detection_error(api_wrong: Translation):
    result = api_wrong.language_detection("Text to detection", "en", ["amazon"])
    assert "errors" in result

#!/usr/bin/env python3
"""Tests for Audio API"""
from test.api.utils import get_api_key

import pytest
from edenai import Audio


@pytest.fixture
def api():
    return Audio(get_api_key())


@pytest.fixture
def api_wrong():
    return Audio("123")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "speech_to_text",
            "https://api.edenai.run/v1/pretrained/audio/speech_recognition",
        ),
        (
            "text_to_speech",
            "https://api.edenai.run/v1/pretrained/audio/text_to_speech",
        ),
    ],
)
def test_endpoints(api: Audio, test_input, expected):
    assert api.get_endpoint_url(test_input) == expected

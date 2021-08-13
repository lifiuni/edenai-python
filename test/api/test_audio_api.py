#!/usr/bin/env python3
"""Tests for Audio API"""
from pathlib import Path
from test.api.utils import get_api_key

import pytest
from edenai import Audio

test_audio = Path(__file__).parent.joinpath("OSR_us_000_0010_8k.wav")


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


@pytest.mark.skip_internet_tests
def test_speech_to_text(api: Audio):
    result = api.speech_to_text( test_audio, "en-US",["amazon"])

    assert len(result["Amazon Web Services"]) > 0


@pytest.mark.skip_internet_tests
def test_text_to_speech(api: Audio):
    result = api.text_to_speech(
        "Hello, my name is John Snow", "en-US", ["amazon"], "MALE"
    )

    assert len(result["Amazon Web Services"]) > 0


@pytest.mark.skip_internet_tests
def test_speech_to_text_error(api_wrong: Audio):
    result = api_wrong.speech_to_text( test_audio, "en-US", ["amazon"])
    assert "errors" in result


@pytest.mark.skip_internet_tests
def test_text_to_speech_error(api_wrong: Audio):
    result = api_wrong.text_to_speech(
        "Hello, my name is John Snow", "en-US", ["amazon"], "MALE"
    )
    assert "errors" in result

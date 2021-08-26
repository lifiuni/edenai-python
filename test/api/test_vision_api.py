#!/usr/bin/env python3
"""Tests for Vision API"""

from pathlib import Path

from test.api.utils import get_api_key

import pytest
from edenai import Vision

test_img = Path(__file__).parent.joinpath("text_image.png")


@pytest.fixture
def api():
    return Vision(get_api_key())


@pytest.fixture
def api_wrong():
    return Vision("123")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "face_detection",
            "https://api.edenai.run/v1/pretrained/vision/face_detection",
        ),
        (
            "object_detection",
            "https://api.edenai.run/v1/pretrained/vision/object_detection",
        ),
        (
            "explicit_content_detection",
            "https://api.edenai.run/v1/pretrained/vision/explicit_content_detection",
        ),
    ],
)
def test_endpoints(api: Vision, test_input, expected):
    assert api.get_endpoint_url(test_input) == expected


@pytest.mark.skip_internet_tests
def test_explicit_content_detection(api: Vision):
    result = api.explicit_content_detection(providers=["amazon", "ibm"], file=test_img)

    assert len(result["Amazon Web Services"]) > 0


@pytest.mark.skip_internet_tests
def test_face_detection(api: Vision):
    result = api.face_detection(providers=["amazon", "microsoft"], file=test_img)

    assert len(result["Amazon Web Services"]) > 0


@pytest.mark.skip_internet_tests
def test_object_detection(api: Vision):
    result = api.object_detection(
        providers=["amazon", "ibm"], file=test_img
    )

    assert len(result["Amazon Web Services"]) > 0


@pytest.mark.skip_internet_tests
def test_explicit_content_detection_error(api_wrong: Vision):
    result = api_wrong.explicit_content_detection(
        providers=["amazon", "ibm"], file=test_img
    )

    assert "errors" in result


@pytest.mark.skip_internet_tests
def test_face_detection_error(api_wrong: Vision):
    result = api_wrong.face_detection(providers=["amazon", "ibm"], file=test_img)
    assert "errors" in result


@pytest.mark.skip_internet_tests
def test_object_detection_error(api_wrong: Vision):
    result = api_wrong.object_detection(
        providers=["amazon", "ibm"], file=test_img
        )
    assert "errors" in result

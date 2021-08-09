#!/usr/bin/env python3
"""Tests for OCR API"""
from pathlib import Path
from test.api.utils import get_api_key

import pytest
from edenai import OCR

invoice_file = Path(__file__).parent.joinpath("invoice.jpg")


@pytest.fixture
def api():
    return OCR(get_api_key())


@pytest.fixture
def api_wrong():
    return OCR("123")


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "basic",
            "https://api.edenai.run/v1/pretrained/vision/ocr",
        ),
        (
            "invoice",
            "https://api.edenai.run/v1/pretrained/ocr/ocr_invoice",
        ),
    ],
)
def test_endpoints(api: OCR, test_input, expected):
    assert api.get_endpoint_url(test_input) == expected


@pytest.mark.skip_internet_tests
def test_basic(api: OCR):
    result = api.basic(file=invoice_file, language="en-US", providers=["amazon"])

    assert len(result["Amazon Web Services"]) > 0
    assert isinstance(result["Amazon Web Services"], str)


@pytest.mark.skip_internet_tests
def test_invoice(api: OCR):
    result = api.invoice(file=invoice_file, language="en-US", providers=["mindee"])

    assert len(result["Mindee"]) > 0
    assert isinstance(result["Mindee"], dict)


@pytest.mark.skip_internet_tests
def test_translation_error(api_wrong: OCR):
    result = api_wrong.basic(file=invoice_file, language="en-US", providers=["amazon"])
    assert "errors" in result


@pytest.mark.skip_internet_tests
def test_language_detection_error(api_wrong: OCR):
    result = api_wrong.invoice(
        file=invoice_file, language="en-US", providers=["amazon"]
    )
    assert "errors" in result

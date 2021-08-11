#!/usr/bin/env python3
"""Tests for API Base class"""

import pytest

from edenai.api.api_base import ApiBase


@pytest.fixture
def api_base():
    return ApiBase("123")


def test_api_key_getter(api_base: ApiBase):
    assert api_base.api_key == "Bearer 123"


def test_api_key_setter(api_base: ApiBase):
    api_base.api_key = "321"
    assert api_base.api_key == "Bearer 321"


def test_post_headers(api_base: ApiBase):
    assert api_base.post_headers == {"Authorization": "Bearer 123"}


def test_get_endpoint_url_correct_endpoint(api_base: ApiBase):
    api_base.endpoints["test"] = "url"

    assert (
        api_base.get_endpoint_url("test") == "https://api.edenai.run/v1/pretrained/url"
    )


def test_get_endpoint_url_incorrect_endpoint(api_base: ApiBase):
    with pytest.raises(KeyError) as e:
        api_base.get_endpoint_url("endpoint")

        assert "name: endpoint" in str(e.value)

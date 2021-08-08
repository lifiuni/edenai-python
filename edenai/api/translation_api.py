#!/usr/bin/env python3
"""Endpoints for the Translation API"""
from typing import Any, Dict, List, Tuple, Union

from edenai.utils.api_requests import post

from .api_base import ApiBase


class Translation(ApiBase):
    """
    Implementation for the Translation API

    Documentation: https://api.edenai.run/v1/redoc/#tag/Translation

    >>> from edenai import Translation
    >>> audio_apis = Translation('<your_api_key>')
    """

    root_endpoint = "text/{}"
    endpoints = {
        "translation": "automatic_translation",
        "language_detection": "language_detection",
    }

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = self.base_url.format(self.root_endpoint)

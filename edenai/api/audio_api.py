#!/usr/bin/env python3
"""Endpoints for the Audio API"""
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from edenai.utils.api_requests import post

from .api_base import ApiBase


class Audio(ApiBase):
    """
    Implementation for the Audio API

    Documentation: https://api.edenai.run/v1/redoc/#tag/Speech

    >>> from edenai import Audio
    >>> audio_apis = Audio('<your_api_key>')
    """

    root_endpoint = "audio/{}"
    endpoints = {
        "speech_to_text": "speech_recognition",
        "text_to_speech": "text_to_speech",
    }

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = self.base_url.format(self.root_endpoint)

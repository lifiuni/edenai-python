#!/usr/bin/env python3
"""Requests via httpx library"""
from typing import Dict, Any
import json

import httpx


def post(url: str, headers: Dict[str, str], payload: Dict[str, Any]) -> httpx.Response:
    """POST requests via sync httpx

    :param str url: endpoint url
    :param dict headers: headers for the request
    :param dict payload: payload data for request,
    :returns: httpx.Response

    """
    return httpx.post(url, headers=headers, data=json.dumps(payload))

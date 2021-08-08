#!/usr/bin/env python3
"""Requests via httpx library"""
import json
from pathlib import Path
from typing import Any, Dict, Union

import httpx


def post(
    url: str,
    headers: Dict[str, str],
    payload: Dict[str, Any],
    files: Union[str, Path] = None,
) -> httpx.Response:
    """POST requests via sync httpx

    :param str url: endpoint url
    :param dict headers: headers for the request
    :param dict payload: payload data for request
    :param str|Path file: file to upload, default None
    :returns: httpx.Response

    """
    files = _get_files_for_httpx_upload(files)
    return httpx.post(url, headers=headers, data=payload)


def _get_files_for_httpx_upload(files):
    if files is None:
        return None
    return {"upload-file": open(files, "rb")}

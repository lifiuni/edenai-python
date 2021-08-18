#!/usr/bin/env python3
"""Endpoints for the Vision API"""
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from edenai.utils.api_requests import post

from .api_base import ApiBase


class Vision(ApiBase):
    """
    Implementation for the Vision API

    Documentation: https://api.edenai.run/v1/redoc/#tag/Vision

    >>> from edenai import Vision
    >>> vision_apis = Vision('<your_api_key>')
    """

    root_endpoint = "vision/{}"
    endpoints = {
        "face_detection": "face_detection",
        "object_detection": "object_detection",
        "explicit_content_detection": "explicit_content_detection",
    }

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = self.base_url.format(self.root_endpoint)

    def explicit_content_detection(
        self, file: Union[str, Path], providers: List[str]
    ) -> Dict[str, Dict[str, Any]]:
        """Explicit Content Detection detects adult only content in videos,
        who is generally inappropriate for people under the age of 18 and
        includes nudity, sexual activity and pornography ...

        https://api.edenai.run/v1/redoc/#operation/Explicit%20Content%20Detection

        >>> from edenai import Vision
        >>> vision_apis = Vision('<your_api_key'>)
        >>> result = vision_apis.explicit_content_detection(
        ...    providers=["amazon", "ibm"],
        ...    file="Picture/example1.jpg")

        :param Path|str file: A path to an image (pdf, jpg, jpeg, png, tiff),
            must be str or Path
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of tuples {"google" : (result), "microsoft" : (result), …}
        """
        response = post(
            url=self.get_endpoint_url("explicit_content_detection"),
            headers=self.post_headers,
            payload={"providers": str(providers)},
            files=file,
        ).json()

        result = {}

        try:
            results = response["result"]
        except KeyError:
            return response

        for i in results:
            provider = i.get("solution_name")
            js_result = i.get("result", {})
            result[provider] = js_result

        return result

    def face_detection(
        self, file: Union[str, Path], providers: List[str]
    ) -> Dict[str, Dict[str, Any]]:
        """Face Detection is a computer technology being used in a variety of
        applications that identifies human faces in digital images.

        https://api.edenai.run/v1/redoc/#operation/Face%20Detection

        >>> from edenai import Vision
        >>> vision_apis = Vision('<your_api_key'>)
        >>> result = vision_apis.face_detection(
        ...    providers=["amazon", "ibm"],
        ...    file="Picture/example1.jpg")

        :param Path|str file: A path to an image (pdf, jpg, jpeg, png, tiff),
            must be str or Path
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of tuples {"google" : (result), "microsoft" : (result), …}
        """
        response = post(
            url=self.get_endpoint_url("explicit_content_detection"),
            headers=self.post_headers,
            payload={"providers": str(providers)},
            files=file,
        ).json()

        result = {}

        try:
            results = response["result"]
        except KeyError:
            return response

        for i in results:
            provider = i.get("solution_name")
            js_result = i.get("result", {})
            result[provider] = js_result

        return result

    def object_detection(
        self, file: Union[str, Path], providers: List[str] 
    ) -> Dict[str, Dict[str, Any]]:
        """Object Detection is a computer vision technique that allows us
        to identify and locate objects in an image or video

        https://api.edenai.run/v1/redoc/#operation/Object%20Detection

        >>> from edenai import Vision
        >>> vision_apis = Vision('<your_api_key'>)
        >>> result = vision_apis.object_detection(
        ...    providers=["amazon", "ibm"],
        ...    file="Picture/example1.jpg")

        :param Path|str file: A path to an image (pdf, jpg, jpeg, png, tiff),
            must be str or Path
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of tuples {"google" : (result), "microsoft" : (result), …}
        """
        response = post(
            url=self.get_endpoint_url("explicit_content_detection"),
            headers=self.post_headers,
            payload={
                "providers": str(providers),
            },
            files=file,
        ).json()

        result = {}

        try:
            results = response["result"]
        except KeyError:
            return response

        for i in results:
            provider = i.get("solution_name")
            js_result = i.get("result", {})
            result[provider] = js_result

        return result

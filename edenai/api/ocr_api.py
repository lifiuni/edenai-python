#!/usr/bin/env python3
"""Endpoints for the OCR API"""
from pathlib import Path
from typing import Any, Dict, List, Union

from edenai.utils.api_requests import post

from .api_base import ApiBase


class OCR(ApiBase):
    """
    Implementation for the OCR API

    Documentation: https://api.edenai.run/v1/redoc/#tag/OCR

    >>> from edenai import OCR
    >>> ocr_apis = OCR('<your_api_key>')
    """

    root_endpoint = "vision/{}"
    endpoints = {
        "basic": "ocr",
        "invoice": "ocr_invoice",
    }

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = self.base_url.format(self.root_endpoint)

    def basic(
        self,
        file: Union[Path, str],
        language: str,
        providers: List[str],
    ) -> Dict[str, str]:
        """Optical Character Recognition or optical character reader (OCR)
        is the electronic or mechanical conversion of images of typed,
        handwritten or printed text into machine-encoded text, whether from
        a scanned document, a photo of a document.

        https://api.edenai.run/v1/redoc/#operation/OCR

        >>> from edenai import OCR
        >>> ocr_apis = OCR('<your_api_key'>)
        >>> result = ocr_apis.basic(
        ...    providers=["amazon", "ibm"],
        ...    language="en-US",
        ...    file="Images/image.png")

        :param str|Path file: Path to a file image to analyse (ex: pdf, jpg,
            jpeg, png, tiff)
        :param str language: Language codec expected (ex: en-US, fr-FR)
        :param list(str) providers: Providers, non-empty Provider
            to compare (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of strings {"google": final_text, "microsoft": final_text, …}

        """
        payload = {
            "providers": str(providers),
            "language": language,
        }
        response = post(
            url=self.get_endpoint_url("basic"),
            headers=self.post_headers,
            payload=payload,
            files=file,
        ).json()
        result = {}

        try:
            results = response["result"]
        except KeyError:
            return response

        for i in results:
            provider = i.get("solution_name")
            result[provider] = i.get("final_text", "")

        return result

    def invoice(
        self,
        file: Union[Path, str],
        language: str,
        providers: List[str],
    ) -> Dict[str, Dict[str, Any]]:
        """The OCR Invoice API enables customers to take invoices in a variety
        of formats and return structured data to automate the invoice processing.

        https://api.edenai.run/v1/redoc/#operation/OCR%20Invoice

        >>> from edenai import OCR
        >>> ocr_apis = OCR('<your_api_key'>)
        >>> result = ocr_apis.invoice(
        ...    providers=["amazon", "ibm"],
        ...    language="en-US",
        ...    file="Images/image.png")

        :param str|Path file: Path to a file image to analyse
            (ex: pdf, jpg, jpeg, png, tiff)
        :param str language: Language codec expected (ex: en-US, fr-FR)
        :param list(str) providers: Providers, non-empty Provider
            to compare (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of dicts {"google": {result}, "microsoft": {result}, …}

        """
        payload = {
            "providers": str(providers),
            "language": language,
        }
        response = post(
            url=self.get_endpoint_url("invoice"),
            headers=self.post_headers,
            payload=payload,
            files=file,
        ).json()

        result = {}

        try:
            results = response["result"]
        except KeyError:
            return response

        for i in results:
            provider = i.get("solution_name")
            result[provider] = i.get("normalized_result", {})

        return result

    def get_endpoint_url(self, endpoint_name: str) -> str:
        """Returning endpoint URL by endpoint name

        :param str endpoint_name: endpoint name, e.g. ner or sentiment_analysys
        """
        if endpoint_name == "invoice":
            return "https://api.edenai.run/v1/pretrained/ocr/ocr_invoice"
        try:
            return self.base_url.format(self.endpoints[endpoint_name])
        except KeyError:
            raise KeyError("Unknown endpoint name: {}".format(endpoint_name))

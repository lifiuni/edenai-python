#!/usr/bin/env python3
"""Endpoints for the Translation API"""
from typing import Dict, List, Tuple

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

    def translation(
        self,
        text_to_translate: str,
        source_language: str,
        target_language: str,
        providers: List[str],
    ) -> Dict[str, str]:
        """Machine translation refers to the translation of a text
        into another language using rules, statics or ml technics.

        https://api.edenai.run/v1/redoc/#operation/Automatic%20Translation

        >>> from edenai import Translation
        >>> translation_apis = Translation('<your_api_key'>)
        >>> result = translation_apis.translation(
        ...    text_to_translate="Hello, my name is John"
        ...    providers=["amazon", "ibm"],
        ...    source_language="en-US",
        ...    target_language="fr-FR")

        :param str text_to_translate: Text to translate
        :param str source_language: Language codec of text
            (ex: fr-FR (French), en-US (English), es-ES (Spanish))
        :param str target_language: Language codec of text
            (ex: fr-FR (French), en-US (English), es-ES (Spanish))
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of strings {"google" : translated_text, "microsoft" : translated_text, …}
        """
        payload = {
            "providers": str(providers),
            "text_to_translate": text_to_translate,
            "source_language": source_language,
            "target_language": target_language,
        }
        response = post(
            url=self.get_endpoint_url("translation"),
            headers=self.post_headers,
            payload=payload,
        ).json()

        result = {}

        try:
            results = response["result"]
        except KeyError:
            return response

        for i in results:
            provider = i.get("solution_name")
            result[provider] = i.get("result", {}).get("translated_text")

        return result

    def language_detection(
        self,
        text: str,
        providers: List[str],
    ) -> Dict[str, Tuple[List, List]]:
        """Language Detection or language guessing is the algorithm of
        determining which natural language given content is in.

        https://api.edenai.run/v1/redoc/#operation/Language%20Detection

        >>> from edenai import Translation
        >>> translation_apis = Translation('<your_api_key'>)
        >>> result = translation_apis.language_detection(
        ...    text="Hello, my name is John"
        ...    providers=["amazon", "ibm"],
        ...    )

        :param str text: Text to analyze
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of tuples {"google" : (languages, confidences), "microsoft" : (languages, confidences), …}
        """
        payload = {
            "providers": str(providers),
            "text": text,
        }
        response = post(
            url=self.get_endpoint_url("language_detection"),
            headers=self.post_headers,
            payload=payload,
        ).json()

        result = {}

        try:
            results = response["result"]
        except KeyError:
            return response

        for i in results:
            provider = i.get("solution_name")
            res = i.get("result", {})
            result[provider] = (res.get("languages", []), res.get("confidences", []))

        return result

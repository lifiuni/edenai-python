#!/usr/bin/env python3
"""Endpoints for the Text API"""
from typing import Dict, List, Tuple

from edenai.utils.httpx_requests import post

from .api_base import ApiBase


class Text(ApiBase):
    """Implementation for the Text API

    Documentation: https://api.edenai.run/v1/redoc/#tag/Text

    >>> from edenai import Text
    >>> nlp_apis = Text('<your_api_key>')
    """

    root_endpoint = "text/{}"
    endpoints = {
        "ner": "named_entity_recognition",
        "sentiment_analysys": "sentiment_analysis",
        "syntax_analysis": "syntax_analysis",
        "keyword_extraction": "keyword_extraction",
    }

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = self.base_url.format(self.root_endpoint)

    def ner(
        self, entities_to_find: str, language: str, text: str, providers: List[str]
    ) -> Dict[str, Tuple[List, List]]:
        """Named Entity Recognition (also called entity identification or
        entity extraction) is an information extraction technique that
        automatically identifies named entities in a text and classifies
        them into predefined categories.

        https://api.edenai.run/v1/redoc/#operation/Named%20Entity%20Recognition

        >>> from edenai import Text
        >>> nlp_apis = Text('<your_api_key'>)
        >>> result = nlp_apis.ner(
            providers=["amazon", "ibm"],
            text="I am angry today",
            entities_to_find="",
            language="en-US"

        )

        :param str entities_to_find: Entities to find [ 1 .. 1000 ] characters
        :param str language: Language codec of text (ex: fr-FR (French),
            en-US (English), es-ES (Spanish))
        :param str text: Text to analyze
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of tuples {"google" : ([entities], [importance]), "microsoft" : ([entities], [importance]), …}
        """
        payload = {
            "providers": providers,
            "text": text,
            "entities_to_find": entities_to_find,
            "language": language,
        }

        response = post(
            url=self.get_endpoint_url("ner"), headers=self.post_headers, payload=payload
        ).json()

        result = {}

        for i in response:
            provider = i.get("solution_name")
            result[provider] = (i.get("entities", []), i.get("importances", []))

        return result

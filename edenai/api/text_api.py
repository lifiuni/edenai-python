#!/usr/bin/env python3
"""Endpoints for the Text API"""
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
    }

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = self.base_url.format(self.root_endpoint)

    def ner(self, entities_to_find: str, language: str, text: str, providers: str):
        """Named Entity Recognition (also called entity identification or
        entity extraction) is an information extraction technique that
        automatically identifies named entities in a text and classifies
        them into predefined categories.

        :param entities_to_find:
        :param language:
        :param text:
        :param providers:

        """
        pass

#!/usr/bin/env python3
"""Endpoints for the Text API"""
from typing import Any, Dict, List, Tuple

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
        ...    providers=["amazon", "ibm"],
        ...    text="I am angry today",
        ...    entities_to_find="",
        ...    language="en-US")

        :param str entities_to_find: Entities expected
        :param str language: Language codec of text (ex: fr-FR (French),
            en-US (English), es-ES (Spanish))
        :param str text: Text to analyze
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of tuples {"google" : ([entities], [importance]), "microsoft" : ([entities], [importance]), …}
        """
        payload = {
            "providers": str(providers),
            "text": text,
            "entities_to_find": entities_to_find,
            "language": language,
        }

        response = post(
            url=self.get_endpoint_url("ner"), headers=self.post_headers, payload=payload
        ).json()

        result = {}

        for i in response["result"]:
            provider = i.get("solution_name")
            js_result = i.get("result", {})
            result[provider] = (
                js_result.get("entities", []),
                js_result.get("importances", []),
            )

        return result

    def sentiment_analysys(
        self,
        sentiments_to_find: List[str],
        language: str,
        text: str,
        providers: List[str],
        fake_call: bool = True,
    ) -> Dict[str, Tuple[List, List]]:
        """Sentiment analysis API extracts sentiment in a given string of text.
        Sentiment analysis, also called 'opinion mining', uses natural language
        processing, text analysis and computational linguistics to identify and
        detect subjective information from the input text.

        https://api.edenai.run/v1/redoc/#operation/Sentiment%20Analysis

        >>> from edenai import Text
        >>> nlp_apis = Text('<your_api_key'>)
        >>> result = nlp_apis.sentiment_analysys(
        ...    providers=["amazon", "ibm"],
        ...    text="I am angry today",
        ...    sentiments_to_find=["neutral"],
        ...    language="en-US")

        :param list(str) sentiments_to_find: Sentiment expected
        :param str language: Language codec of text (ex: fr-FR (French),
            en-US (English), es-ES (Spanish))
        :param str text: Text to analyze
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :param bool fake_call: boolean (Fake call), default: True
        :returns: dictionary of tuples {"google" : ([sentiments], [sentiment_rate]), "microsoft" : ([sentiments], [sentiment_rate]), …}
        """
        payload = {
            "providers": str(providers),
            "text": text,
            "sentiments_to_find": str(sentiments_to_find),
            "language": language,
            "fake_call": fake_call,
        }

        response = post(
            url=self.get_endpoint_url("sentiment_analysys"),
            headers=self.post_headers,
            payload=payload,
        ).json()

        result = {}

        for i in response["result"]:
            provider = i.get("solution_name")
            js_result = i.get("result", {})
            result[provider] = (
                js_result.get("sentiments", []),
                js_result.get("sentiment_rate", []),
            )

        return result

    def syntax_analysys(
        self,
        language: str,
        text: str,
        providers: List[str],
        fake_call: bool = True,
    ) -> Dict[str, Dict[str, Any]]:
        """Syntax analysis consists principaly in highlighting the structure of a text.

        https://api.edenai.run/v1/redoc/#operation/Syntax%20Analysis

        >>> from edenai import Text
        >>> nlp_apis = Text('<your_api_key'>)
        >>> result = nlp_apis.syntax_analysys(
        ...    providers=["amazon", "ibm"],
        ...    text="I am angry today",
        ...    language="en-US")

        :param str language: Language codec of text (ex: fr-FR (French),
            en-US (English), es-ES (Spanish))
        :param str text: Text to analyze
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :param bool fake_call: boolean (Fake call), default: True
        :returns: dictionary of tuples {"google" : (result), "microsoft" : (result), …}
        """
        payload = {
            "providers": str(providers),
            "text": text,
            "language": language,
            "fake_call": fake_call,
        }

        response = post(
            url=self.get_endpoint_url("syntax_analysis"),
            headers=self.post_headers,
            payload=payload,
        ).json()

        result = {}

        for i in response["result"]:
            provider = i.get("solution_name")
            js_result = i.get("result", {})
            result[provider] = js_result

        return result

    def keyword_extraction(
        self,
        keywords_to_find: List[str],
        language: str,
        text: str,
        providers: List[str],
        fake_call: bool = True,
    ) -> Dict[str, Dict[str, Any]]:
        """Keyword extraction (also known as keyword detection or keyword analysis)
        is a text analysis technique that consists of automatically extracting
        the most important words and expressions in a text.

        https://api.edenai.run/v1/redoc/#operation/Keyword%20Extraction

        >>> from edenai import Text
        >>> nlp_apis = Text('<your_api_key'>)
        >>> result = nlp_apis.keyword_extraction(
        ...    keywords_to_find=['neutral'],
        ...    providers=["amazon", "ibm"],
        ...    text="I am angry today",
        ...    language="en-US")

        :param list(str) keywords_to_find: Keyword expected
        :param str language: Language codec of text (ex: fr-FR (French),
            en-US (English), es-ES (Spanish))
        :param str text: Text to analyze
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :param bool fake_call: boolean (Fake call), default: True
        :returns: dictionary of tuples {"google" : ([keywords], [importances]), "microsoft" : ([keywords], [importances]), …}
        """
        payload = {
            "keywords_to_find": str(keywords_to_find),
            "providers": str(providers),
            "text": text,
            "language": language,
            "fake_call": fake_call,
        }

        response = post(
            url=self.get_endpoint_url("keyword_extraction"),
            headers=self.post_headers,
            payload=payload,
        ).json()

        result = {}

        for i in response["result"]:
            provider = i.get("solution_name")
            js_result = i.get("result", {})
            result[provider] = (
                js_result.get("keywords", []),
                js_result.get("importances", []),
            )

        return result

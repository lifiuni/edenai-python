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

    def speech_to_text(
        self,
        text_to_find: List[str],
        language: str,
        file: Union[Path, str],
        providers: List[str],
    ) -> Dict[str, Dict[str, Any]]:
        """Speech recognition is technology that can recognize spoken words,
        which can then be converted to text.

        https://api.edenai.run/v1/redoc/#operation/Speech%20Recognition

        >>> from edenai import Audio
        >>> audio_apis = Audio('<your_api_key'>)
        >>> result = audio_apis.speech_to_text(
        ...    text_to_find=["some text"],
        ...    providers=["amazon", "ibm"],
        ...    file="Audio/example1.wav",
        ...    language="en-US")

        :param Path|str file: File to analyse (ex: mp3, wav, m4a)
        :param str language: Language codec expected
            (ex: fr-FR (French), en-US (English), es-ES (Spanish), nl-NL Dutch (Netherlands))
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of tuples {"google" : (result), "microsoft" : (result), …}
        """
        payload = {
            "providers": str(providers),
            "text_to_find": str(text_to_find),
            "language": language,
        }
        response = post(
            url=self.get_endpoint_url("speech_to_text"),
            headers=self.post_headers,
            files=file,
            payload=payload,
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

    def text_to_speech(
        self, text: str, language: str, providers: List[str], option: str
    ) -> Dict[str, Dict[str, Any]]:
        """Text-to-speech (TTS) system converts normal language text into speech.

        https://api.edenai.run/v1/redoc/#operation/Text%20To%20Speech

        >>> from edenai import Audio
        >>> audio_apis = Audio('<your_api_key'>)
        >>> result = audio_apis.text_to_speech(
        ...    text="Some text",
        ...    option=FEMALE,
        ...    providers=["amazon", "ibm"],
        ...    language="en-US")

        :param str text: Text to transform
        :param str option: Voice gender selected (ex: FEMALE ou MALE)
        :param str language: Language codec expected
            (ex: fr-FR (French), en-US (English), es-ES (Spanish), nl-NL Dutch (Netherlands))
        :param list(str) providers: Providers, non-empty Provider to compare
            (ex: ['amazon', 'microsoft', 'ibm','google'])
        :returns: dictionary of tuples {"google" : (result), "microsoft" : (result), …}
        """
        payload = {
            "providers": str(providers),
            "language": language,
            "option": option,
            "text": text,
        }
        response = post(
            url=self.get_endpoint_url("text_to_speech"),
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
            js_result = i.get("result", {})
            result[provider] = js_result

        return result

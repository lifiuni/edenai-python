#!/usr/bin/env python3
"""
Base class for all API calls
"""
from typing import Dict


class ApiBase:
    """Base class for all API calls

    >>> class A(ApiBase):
    ...     def __init__(api_key, *args, **kwargs):
    ...         super().__init__(api_key, *args, **kwargs)
    ...
    ...     def foo(self):
    ...         endpoint_url = self.base_url.format('endpoint')

    """

    base_url = "https://api.edenai.run/v1/pretrained/{}"

    def __init__(self, api_key: str, *args, **kwargs) -> None:
        """ApiBase class initialisation

        :param str api_key: Your API key, see https://api.edenai.run/v1/redoc/
        :returns: None
        """
        self._api_key = api_key

    @property
    def api_key(self) -> str:
        """A string for the authorizatioin

        :returns: a string like: "Bearer <your_api_key>"
        """
        return "Bearer {}".format(self._api_key)

    @api_key.setter
    def api_key(self, api_key: str) -> None:
        """Set the new API key

        :param str api_key: Your API key, see https://api.edenai.run/v1/redoc/
        :returns: None
        """
        self._api_key = api_key

    @property
    def post_headers(self) -> Dict[str, str]:
        """Headers for the POST API requests

        :returns: Dict object with strings as keys and values
        """
        return {"Authorization": self.api_key}

#!/usr/bin/env python3
"""Different tools for API test"""
import os
from dotenv import load_dotenv


def get_api_key():
    """Read .env file and get API_KEY variable"""
    load_dotenv()
    return os.getenv("API_KEY", "API KEY")

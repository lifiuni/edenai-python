# Imports
import json
import requests
import numpy as np


class Text():
    def __init__(self, api_key):
        self.headers = {'Authorization': f'Bearer {api_key}'}
        self.host = "https://dev-api.edenai.run/" 
        
    def translate(self, text, providers, source_language, target_language):
        response = requests.post(self.host+"v1/pretrained/text/automatic_translation" , 
                                    headers=self.headers,
                                    data={'providers': providers,
                                          'text_to_translate': text,
                                          'source_language': source_language,
                                          'target_language': target_language})

        result = json.loads(response.text)["result"]
        return result[0]["result"]["translated_text"]
    
    def keywords_extraction(self, text, providers, language):
        response = requests.post(self.host+"v1/pretrained/text/keyword_extraction" , 
                            headers=self.headers,
                            data={'providers': providers,
                                  'text': text[:1000],
                                  'language': language})

        result = json.loads(response.text)["result"]
        return result[0]["result"]["keywords"]

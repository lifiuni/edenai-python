# Imports
import json
import requests
import numpy as np


class Vision():
    def __init__(self, api_key):
        self.headers = {'Authorization': f'Bearer {api_key}'}
        self.host = "https://dev-api.edenai.run/"        

    def ocr(self, document, providers, language):
        with open(document, 'rb') as f:
            response = requests.post(self.host+"v1/pretrained/vision/ocr" , 
                                    headers=self.headers,
                                    data={'providers': providers,
                                           'language': language},
                                    files={"files": f})
        result = json.loads(response.text)["result"]
        return result[0]["final_text"]
    


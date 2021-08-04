# Imports
import json
import requests
import numpy as np

   
class Pipeline():
    def __init__(self, api_key):
        self.vision = Vision(api_key)
        self.text = Text(api_key)
    
    def run(self, data, pipeline):
        data_inter = data
        for application, arguments in pipeline:
            for block in [self.vision, self.text]:
                if application in dir(block) :
                    print(application, block, dir(block), arguments)
                    data_inter = getattr(block, application)(data_inter, **arguments)
       
        return data_inter
        

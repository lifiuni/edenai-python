import requests

# You can find the documentation here : https://api.edenai.run/v1/redoc/#section/How-it-works

#Enter your API Token
headers = {  'Authorization': 'Bearer your API Key'}

# Select API
url = 'https://api.edenai.run/v1/pretrained/vision/ocr_invoice'

# Select providers
payload = {'providers': '[\'mindee\', \'microsoft\']','language': 'en-US'}

# Select file to test
files = [  ('files', open('Picture/example.jpg','rb'))]

# Request to Eden AI
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))

import requests

# You can find the documentation here : https://api.edenai.run/v1/redoc/#section/How-it-works

#Enter your API Token
headers = {  'Authorization': 'Bearer your API Key'}

# Select API
url = 'https://api.edenai.run/v1/pretrained/vision/explicit_content_detection'

# Select providers
payload = {'providers': '[\'google_cloud\', \'microsoft\', \'aws\', \'ibm\']'}

# Select file to test
files = [  ('files', open('Picture/example.jpg','rb'))]

# Request to Eden AI
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))

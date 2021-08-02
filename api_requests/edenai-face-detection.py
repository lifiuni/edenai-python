import requests

# You can find the documentation here : https://api.edenai.run/v1/redoc/#section/How-it-works

#Enter your API Token
headers = {  'Authorization': 'Bearer your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://api.edenai.run/v1/pretrained/vision/face_detection'

# Select providers
payload = {'providers': '[\'google\', \'microsoft\', \'aws\']'}

# Select file to test
files = [  ('files', open('Picture/example.jpg','rb'))]

# Request to Eden AI
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))

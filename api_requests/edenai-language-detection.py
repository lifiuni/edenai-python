import requests

# You can find the documentation here : https://api.edenai.run/v1/redoc/#section/How-it-works

#Enter your API Token
headers = {'Authorization': 'Bearer your API Key'}

# Select API
url = 'https://api.edenai.run/v1/pretrained/text/language_detection

# Select providers, and text to analyze
payload = {'providers': '[\'google_cloud\', \'microsoft\', \'aws\', \'ibm\']','text':'I am angry today', 'language_to_find': 'en'}

# Request to Eden AI
response = requests.request("POST", url, headers=headers, data = payload)

# Print result
print(response.text.encode('utf8'))

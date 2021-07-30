import requests

# You can find the documentation here : https://api.edenai.run/v1/redoc/

#Enter your API Token
headers = {'Authorization': 'Bearer API Key'}

# Select API
url = 'https://api.edenai.run/v1/pretrained/text/automatic_translation'

# Select providers, and text to translate, and source / target languages
payload = {'providers': '[\'ibm\', \'microsoft\', \'aws\', \'google_cloud\']','text_to_translate':'how are you today', 'source_language': 'en','target_language': 'fr'}

# Request to Eden AI
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))

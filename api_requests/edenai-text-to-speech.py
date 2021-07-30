import requests

# You can find the documentation here : https://api.edenai.run/v1/redoc/#section/How-it-works

#Enter your API Token
headers = {'Authorization': 'Bearer your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://api.edenai.run/v1/pretrained/audio/text_to_speech'

# Select providers, and audio to transcribe
payload = {'providers':'[\'ibm\', \'microsoft\', \'aws\', \'google_cloud\']','text':'Hi, my name is Martin','language':'en-US', 'option':'MALE'}

# Request to Eden AI
response = requests.request("POST", url, headers=headers, data = payload)

# Print result
print(response.text.encode('utf8'))

pip install edenai

from edenai import Text

# Get your API key here: https://app.edenai.run/admin/account
text_apis = Text("Your_API_key")

result = text_apis.sentiment_analysis(
# Available providers and languages here: https://api.edenai.run/v1/redoc/#operation/Language%20Detection
    text="Your text",
    providers=["amazon", "ibm"],
    language="en-US")

print(result) 

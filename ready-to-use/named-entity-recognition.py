pip install edenai

from edenai import Text

# Get your API key here: https://app.edenai.run/admin/account
text_apis = Text("Your_API_key")

result = text_apis.ner(
# Available providers and languages here: https://api.edenai.run/v1/redoc/#operation/Named%20Entity%20Recognition
    text="Your text",
    providers=["amazon", "ibm"],
    language="en-US")

print(result)

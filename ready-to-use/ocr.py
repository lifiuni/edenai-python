pip install edenai

from edenai import OCR

# Get your API key here: https://app.edenai.run/admin/account
ocr_apis = OCR("Your_API_key")

result = ocr_apis.basic(
# Available providers, languages and formats here: https://api.edenai.run/v1/redoc/#operation/OCR
   providers=["google","amazon"],
   language="en-US",
   file="your_image.png")

print(result)

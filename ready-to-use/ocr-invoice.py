pip install edenai

from edenai import OCR

# Get your API key here: https://app.edenai.run/admin/account
ocr_apis = OCR("Your_API_key")

result = ocr_apis.invoice(
# Available providers, languages and formats here: https://api.edenai.run/v1/redoc/#operation/OCR%20Invoice
   providers=["microsoft", "mindee"],
   language="en-US",
   file="your_invoice.pdf")

print(result) 

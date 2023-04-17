import os
from dotenv import load_dotenv
import json
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential

# load environment variables from .env file
load_dotenv()

# get endpoint and key from environment variables
endpoint = os.getenv("FORM_RECOGNIZER_ENDPOINT")
key = os.getenv("FORM_RECOGNIZER_KEY")


# create the client and authenticate with the endpoint and key
form_recognizer_client = FormRecognizerClient(endpoint, AzureKeyCredential(key))
form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))

# replace with the URL of your receipt image
myReceiptUrl = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png"

# recognize receipt data from the image URL
poller = form_recognizer_client.begin_recognize_receipts_from_url(myReceiptUrl)
result = poller.result()

# loop through the recognized results and extract data from the receipt
for receipt in result:
    for name, field in receipt.fields.items():
        if name =='Items':
            print("Receipt Items:")
            for idx, items in enumerate(field.value):
                print("...Item #{}".format(idx + 1))
                for item_name, item in items.value.items():
                    print("....{}: {} has confidence {}".format(item_name, item.value, item.confidence))
        else:
            print("....{}: {} has confidence {}".format(name, field.value, field.confidence))
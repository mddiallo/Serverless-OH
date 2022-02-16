import logging
import requests
import json
import uuid
from datetime import datetime

import azure.functions as func


def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('CreateRating function processed a request.')

    req_body = req.get_json()
    
    # Check product param
    productId = req_body.get('productId')
    if not productId:
        return func.HttpResponse("You need to pass the productId in the request payload.", status_code=400)
    
    # Check user param
    userId = req_body.get('userId')
    if not userId:
        return func.HttpResponse("You need to pass the userId in the request payload.", status_code=400)

    # Check rating param
    rating = req_body.get('rating')
    if rating > 5 or rating < 0:
        return func.HttpResponse("Rating must be between 0 and 5.", status_code=400)

    # Validate product
    productUrl = f"https://serverlessohapi.azurewebsites.net/api/GetProduct?productId={productId}"
    productResponse = requests.get(productUrl)
    if not (productResponse.status_code == 200):
        return func.HttpResponse(f"Product id {productId} not found.", status_code=400)

    # Validate user
    userUrl = f"https://serverlessohapi.azurewebsites.net/api/GetUser?userId={userId}"
    userResponse = requests.get(userUrl)
    if not (userResponse.status_code == 200):
        return func.HttpResponse(f"User id {userId} not found.", status_code=400)

    # Add id value
    req_body['id'] = str(uuid.uuid4())

    # Add timestamp
    now = datetime.now() # current date and time
    req_body['timestamp'] = now.strftime("%Y-%m-%d %H:%M:%S%Z")

    # Store rating in Cosmos
    doc.set(func.Document.from_dict(req_body))

    return func.HttpResponse(
        body=json.dumps(req_body, indent=True),
        mimetype="application/json",
        status_code=200)


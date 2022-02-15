import logging
import os
#import azure.cosmos.cosmos_client as cosmos_client
import azure.functions as func


def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('CreateRating function processed a request.')

    request_body = req.get_body()

    doc.set(func.Document.from_json(request_body))

    # Get the settings
    #cosmos_host = os.environ["COSMOS_HOST"]
    #cosmos_key = os.environ["MASTER_KEY"]
    #cosmos_database = os.environ["DATABASE_ID"]
    #cosmos_container = os.environ["CONTAINER_ID"]

    #client = cosmos_client.CosmosClient(cosmos_host, {'masterKey': cosmos_key} )

    return func.HttpResponse("Rating created", status_code=200)

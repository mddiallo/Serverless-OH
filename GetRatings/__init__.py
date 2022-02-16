import logging
import os
import json
import azure.cosmos.cosmos_client as cosmos_client

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('GetRatings HTTP trigger function processed a request.')

    # Check user id parameter
    userId = req.params.get('userId')
    if not userId:
        return func.HttpResponse("You need to pass the userId in the request payload.", status_code=400)

    # Get the settings
    cosmos_host = os.environ["COSMOS_HOST"]
    cosmos_key = os.environ["MASTER_KEY"]
    cosmos_database = os.environ["DATABASE_ID"]
    cosmos_container = os.environ["CONTAINER_ID"]

    # Connect to Cosmos
    client = cosmos_client.CosmosClient(cosmos_host, {'masterKey': cosmos_key} )
    db = client.get_database_client(cosmos_database)
    container = db.get_container_client(cosmos_container)

    # Query by id
    items = list(container.query_items(
        query="SELECT * FROM c WHERE c.userId=@userId",
            parameters=[
                { "name":"@userId", "value": userId }
            ],
            enable_cross_partition_query=True
        )
    )

    #if len(items) == 0:
    #    return func.HttpResponse("[]", status_code=404)

    return func.HttpResponse(
        body=json.dumps(items, indent=True),
        mimetype="application/json",
        status_code=200)

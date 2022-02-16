import logging
import os
import json
import azure.cosmos.cosmos_client as cosmos_client

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('GetRating HTTP trigger function processed a request.')

    # Check rating id parameter
    ratingId = req.params.get('ratingId')
    if not ratingId:
        return func.HttpResponse("You need to pass the ratingId in the request payload.", status_code=400)

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
        query="SELECT * FROM c WHERE c.id=@id",
            parameters=[
                { "name":"@id", "value": ratingId }
            ],
            enable_cross_partition_query=True
        )
    )

    if len(items) == 0:
        return func.HttpResponse(f"There is no rating with id {ratingId}.", status_code=404)

    # Remove trash fields
    itemCleaned = items[0]

    try:
        del itemCleaned['_rid']
        del itemCleaned['_self']
        del itemCleaned['_etag']
        del itemCleaned['_attachments']
        del itemCleaned['_ts']
    except KeyError:
        pass

    return func.HttpResponse(
        body=json.dumps(itemCleaned, indent=True),
        mimetype="application/json",
        status_code=200)

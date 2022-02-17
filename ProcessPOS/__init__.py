from typing import List
import logging
import json
import uuid
import os
import azure.cosmos.cosmos_client as cosmos_client

import azure.functions as func


def main(events: List[func.EventHubEvent]):

    # Get the settings
    cosmos_host = os.environ["COSMOS_HOST"]
    cosmos_key = os.environ["MASTER_KEY"]
    cosmos_database = os.environ["DATABASE_ID"]
    cosmos_container = "pos"

    # Connect to Cosmos
    client = cosmos_client.CosmosClient(cosmos_host, {'masterKey': cosmos_key} )
    db = client.get_database_client(cosmos_database)
    container = db.get_container_client(cosmos_container)

    for event in events:
        logging.info('Python EventHub trigger processed an event: %s',
                        event.get_body().decode('utf-8'))

        newBody = json.loads(event.get_body().decode('utf-8'))
        newBody['id'] = str(uuid.uuid4())

        container.create_item(newBody)


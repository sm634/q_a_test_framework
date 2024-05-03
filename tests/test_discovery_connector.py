from connectors.elasticsearch_connector import WatsonDiscoveryV2Connector
from utils.files_handler import FileHandler

file_handler = FileHandler()

def test_discovery_connection():
    discovery_instance = WatsonDiscoveryV2Connector()
    query = discovery_instance.test_query
    # get the queries json for a test query.
    file_handler.get_queries_from_json('vodafone_discovery_queries.json')
    collections_list = file_handler.queries_json["collections"]
    # run the test response.
    discovery_instance.query_response(
        query=query,
        collection_ids=collections_list
    )
    test_response = discovery_instance.response
    if test_response is not None:
        print("Response received from Discovery!")
    else:
        print("No response")

    breakpoint()
    return test_response

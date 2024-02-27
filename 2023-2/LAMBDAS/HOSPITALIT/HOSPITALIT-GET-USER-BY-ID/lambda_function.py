import json
from database import Connection
from config import Configuration
from test_data import get_user
""" Configuration """

config = Configuration()
variables = config.assign_variable_environments(False)
connection = Connection(variables, True)


def lambda_handler(event, context):

    try:
        id_of_user = event['multiValueQueryStringParameters']['user'][0]
        response = json.dumps(connection.get_emr_user(id_of_user))
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": response
        }

    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps("Unexpected error, please contact the administrator")
        }


print(lambda_handler(get_user, None))

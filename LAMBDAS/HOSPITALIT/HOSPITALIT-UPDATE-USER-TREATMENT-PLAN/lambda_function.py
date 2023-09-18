import json
from database import Connection
from config import Configuration
from test_data import data_update_2
""" Configuration """

config = Configuration()
variables = config.assign_variable_environments(False)
connection = Connection(variables, True)

def lambda_handler(event, context):
    try:
        id_of_user_to_update = event['multiValueQueryStringParameters']['user'][0]
        new_diagnosis = event['body']['diagnosis'][0]
        new_treatment = None
        try:
            new_treatment = event['body']['treatments'][0]
        except IndexError as e:
            print(f"Treatment without meds")
        connection.update_with_treatment_plan(id_of_user_to_update, new_diagnosis, new_treatment)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps("User updated successfully")
        }
    except Exception as e:
        print(f"Unexpected error, details: {e}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps("Unexpected error, please contact the administrator")
        }

print(lambda_handler(data_update_2, None))
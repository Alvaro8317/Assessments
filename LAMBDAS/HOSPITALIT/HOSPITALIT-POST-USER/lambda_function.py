from database import Connection
from config import Configuration
from test_data import post_user
""" Configuration """

config = Configuration()
variables = config.assign_variable_environments(False)
connection = Connection(variables, True)


def lambda_handler(event, context):
    try:
        user_to_create = event['body']
        id_of_new_user = connection.create_emr_user(user_to_create)
        print('User created successfully')
        response = {"status": "OK", "code": 200, "payload": {
            "message": "User created successfully", "idOfUser": str(id_of_new_user), "userCreated": True}}
        return response
    except Exception as e:
        print(f'Unexpected error: {e}')
        return {"status": "Error", "code": 500, "payload": {"message": "Unexpected error, please check the logs", "userCreated": None}}

lambda_handler(post_user, None)
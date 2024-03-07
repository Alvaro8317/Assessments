import json
from database import Connection
from config import Configuration
from helpers import send_to_generate_medical_formula
""" Configuration """

config = Configuration()
variables = config.assign_variable_environments(False)
connection = Connection(variables, True)


def lambda_handler(event, context):
    print(event)
    try:
        id_of_user_to_update = event['queryStringParameters']['user']
        body = json.loads(event['body'].replace("\\", ""))
        print(body)
        new_diagnosis = body['diagnosis']
        new_treatment = None
        try:
            new_treatment = body['treatments']
            print(new_treatment)
        except IndexError as e:
            print(f"Treatment without meds")
        connection.update_with_treatment_plan(
            id_of_user_to_update, new_diagnosis, new_treatment)
        complete_patient = connection.get_emr_user(id)['patient']
        print("Getting information of this user:", complete_patient)
        if body['generateMedicalFormula']:
            send_to_generate_medical_formula(
                patient=complete_patient['name'], email=complete_patient['contact_info']['email'], medicine=new_treatment, notes=body['adittionalNotes'], pharmacy=body['pharmacy'])
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
            "body": json.dumps(f"Unexpected error {e}")
        }

import boto3
import json
lambda_client = boto3.client('lambda')
arn_lambda = "arn:aws:lambda:us-east-1:648254270796:function:HOSPITALIT-GENERATE-MEDICAL-FORMULA"


def send_to_generate_medical_formula(patient, email, medicine, notes, pharmacy):
    payload = {
        "body": {
            "name_patient": patient,
            "medicines": medicine,
            "additionalNotes": notes,
            "email": email,
            "sendToPharmacy": True,
            "nameOfPharmacy": pharmacy
        }
    }
    response = lambda_client.invoke(
        FunctionName=arn_lambda,
        InvocationType='RequestResponse',
        LogType='Tail',
        Payload=json.dumps(payload),
    )
    print(response)

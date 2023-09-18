import boto3

lambda_client = boto3.client('lambda')
arn_lambda = "arn:aws:lambda:us-east-1:648254270796:function:HOSPITALIT-GENERATE-MEDICAL-FORMULA"


def send_to_generate_medical_formula(patient, medicine, notes):
    payload = {
        "body": {
            "name_patient": patient,
            "medicines": medicine,
            "additionalNotes": notes,
            "sendToPharmacy": True,
            "nameOfPharmacy": "SALUDPLUS"
        }
    }
    response = lambda_client.invoke(
        FunctionName=arn_lambda,
        InvocationType='RequestResponse',
        LogType='Tail',
        lambda_ClientContext='string',
        Payload=payload,
    )
    print(response)

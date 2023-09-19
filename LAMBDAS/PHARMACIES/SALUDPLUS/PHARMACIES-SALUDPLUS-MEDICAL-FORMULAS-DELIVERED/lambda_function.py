import json
import random
from time import sleep
import boto3
client_sqs = boto3.client('sqs')
arn_medical_formulas_not_ready = "https://sqs.us-east-1.amazonaws.com/648254270796/SALUDPLUS"
arn_medical_formulas_ready = "https://sqs.us-east-1.amazonaws.com/648254270796/SALUDPLUS-READY-TO-BE-DELIVERED"


def lambda_handler(event, context):
    response_medical_order = client_sqs.receive_message(
        QueueUrl=arn_medical_formulas_not_ready,
        AttributeNames=[
            'All',
        ],
        MaxNumberOfMessages=1,
        VisibilityTimeout=120,
        WaitTimeSeconds=20,
    )
    print("Validating the order: ", response_medical_order)
    if 'Messages' not in response_medical_order:
        print("There are not pending medical formulas")
        return generate_response(204, 'There are not pending medical formulas')
    if not preparing_medical_order():
        return generate_response(200, 'Meds not enough, please try again later')
    sleep(10)
    print("Order prepared")
    receipt_handle = response_medical_order['Messages'][0]['ReceiptHandle']
    client_sqs.delete_message(
        QueueUrl=arn_medical_formulas_not_ready, ReceiptHandle=receipt_handle)
    if send_to_ready_queue(response_medical_order['Messages'][0]['Body']):
        return generate_response(200, 'Order ready to be delivered')
    return generate_response(500, "There is a problem with the ready queue")


def preparing_medical_order():
    are_there_enough_meds = random.randint(0, 10)
    if are_there_enough_meds in (1, 2, 3):
        return False
    return True


def generate_response(status_code: int, message: str) -> dict:
    return {
        'isBase64Encoded': False,
        'statusCode': status_code,
        'headers':
            {
                'content-type': 'application/json'
            },
        'body': message
    }


def send_to_ready_queue(message):
    try:
        response_to_send = client_sqs.send_message(
            QueueUrl=arn_medical_formulas_ready,
            MessageBody=json.dumps(message))
        print("Sended message", response_to_send)
        return True
    except Exception as e:
        print("Problem with the ready queue, details:" + e)
        return False

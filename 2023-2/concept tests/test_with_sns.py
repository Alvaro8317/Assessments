import json
import boto3

client = boto3.client('sns')
arn = "arn:aws:sns:us-east-1:648254270796:SALUDPLUS"

def lambda_handler(event, context):
    publish_in_sns(event['message'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def publish_in_sns(message):
    response = client.publish(
        TopicArn=arn,
        Message=message,
        Subject="Otro test"
    )
    print(response)

raw_data = {"message": "Test"}
lambda_handler(raw_data, None)
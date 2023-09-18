import json
import boto3
client = boto3.client('sqs')
url_sqs = "https://sqs.us-east-1.amazonaws.com/648254270796/demo-queue"
response = client.send_message(
    QueueUrl=url_sqs,
    MessageBody=json.dumps({"Test": "Hola"}),
)
print(response)
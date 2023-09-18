import json
import boto3
client = boto3.client('sqs')
url_sqs = "https://sqs.us-east-1.amazonaws.com/648254270796/demo-queue"
# response = client.send_message(
#     QueueUrl=url_sqs,
#     MessageBody=json.dumps({"Test": "Hola"}),
# )
# print(response)

response_2 = client.receive_message(
    QueueUrl=url_sqs,
    AttributeNames=[
        'All',
    ],
    MaxNumberOfMessages=1,
    VisibilityTimeout=120,
    WaitTimeSeconds=20,
)
print(json.dumps(response_2, indent=4))
from typing import Union
from boto3 import client
from aws_lambda_powertools import Logger
logger = Logger()
dynamodb_client = client('dynamodb')
table_name = 'Users'
class UserClass():
  @staticmethod
  def create_user(event) -> dict:
    
    item_to_insert_to_table = {
        'IdUser': {'S': str(event["code"])},
        'CompleteName': {'S': f"{event["name"]} {event["lastName"]}"},
        'Password': {'S': event["password"]},
        'Income': {'S': event.get("Income", "")},
        'Country': {'S': event.get("Country", "")},
        'City': {'S': event.get("City", "")},
        'Age': {'S': event.get("Age", "")},
    }
    logger.info(f"User to insert: {item_to_insert_to_table}")
    return dynamodb_client.put_item(TableName = table_name, Item= item_to_insert_to_table)

  @staticmethod
  def validate_user(id_user: Union[str, int]) -> bool:
    response_dynamo = dynamodb_client.get_item(TableName = table_name, Key={'IdUser': {'S': str(id_user)}})
    logger.info(f"Response of searching the user with ID {id_user}: {response_dynamo}")
    if 'Item' in response_dynamo:
        return True
    return False
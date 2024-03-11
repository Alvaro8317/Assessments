from boto3 import client
from aws_lambda_powertools import Logger

logger = Logger()
dynamodb_client = client("dynamodb")
table_name = "Products"


class ProductPersistence:

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_available_products():
        response_with_available_products = dynamodb_client.scan(TableName=table_name)
        logger.info(f"{response_with_available_products}")
        return response_with_available_products["Items"]

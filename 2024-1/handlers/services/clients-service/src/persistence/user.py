from typing import Union
from boto3 import client
from aws_lambda_powertools import Logger

logger = Logger()
dynamodb_client = client("dynamodb")
table_name = "Users"


class UserPersistence:

    def __init__(
        self, id, complete_name, password, age, incomes, country, city
    ) -> None:
        self.id = id
        self.complete_name = complete_name
        self.password = password
        self.incomes = incomes
        self.country = country
        self.city = city
        self.age = age

    def create_user(self) -> dict:

        item_to_insert_to_table = {
            "IdUser": {"S": str(self.id)},
            "CompleteName": {"S": self.complete_name},
            "Password": {"S": self.password},
            "Income": {"S": self.incomes},
            "Country": {"S": self.country},
            "City": {"S": self.city},
            "Age": {"S": self.age},
        }
        response_dynamo = dynamodb_client.put_item(
            TableName=table_name, Item=item_to_insert_to_table
        )
        logger.info(f"Response of DynamoDB: {response_dynamo}")
        return response_dynamo

    def update_user(self) -> dict:
        response_dynamo = dynamodb_client.update_item(
            TableName=table_name,
            Key={"IdUser": {"S": str(self.id)}},
            UpdateExpression="SET CompleteName = :n, Income = :s, Country = :c, City = :i, Age = :a",
            ExpressionAttributeValues={
                ":n": {"S": self.complete_name},
                ":s": {"N": self.incomes},
                ":c": {"S": self.country},
                ":i": {"S": self.city},
                ":a": {"N": self.age},
            },
        )
        logger.info(f"Response of user to update: {response_dynamo}")
        return response_dynamo

    def validate_if_exists_user_with_that_id(self, return_item: bool = False) -> bool:
        response_dynamo = dynamodb_client.get_item(
            TableName=table_name, Key={"IdUser": {"S": str(self.id)}}
        )
        logger.info(
            f"Response of searching the user with ID {self.id}: {response_dynamo}"
        )
        if "Item" in response_dynamo:
            if not return_item:
                return True
            self.complete_name
            self.incomes
            self.country
            self.age
            return True, response_dynamo["Item"]
        return False

    def validate_profile_of_user(self):
        pass
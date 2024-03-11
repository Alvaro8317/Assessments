import json
from boto3 import client
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics
from models import Functions

tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")
client_lambda = client("lambda")


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    if "products_service" in event:
        response_of_microservice = client_lambda.invoke(
            FunctionName=Functions.PRODUCTS.value,
            LogType="Tail",
            Payload=bytes(json.dumps(event), "utf-8"),
        )
        return response_of_microservice["Payload"].read()
    if "client_service" in event:
        response_of_microservice = client_lambda.invoke(
            FunctionName=Functions.CLIENTS.value,
            LogType="Tail",
            Payload=bytes(json.dumps(event), "utf-8"),
        )
        return response_of_microservice["Payload"].read()
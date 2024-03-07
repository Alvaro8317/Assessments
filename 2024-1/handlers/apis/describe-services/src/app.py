from typing import Union
from boto3 import client
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit

app = APIGatewayRestResolver()
tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")
create_response = lambda message: {"message": message}
dynamodb_client = client("dynamodb")
table_name = "BankServices"


@app.get("/")
def get_bank_services() -> dict:
    metrics.add_metric(name="GetBankServicesInvocation", unit=MetricUnit.Count, value=1)
    response = dynamodb_client.scan(TableName=table_name)
    logger.info(response)
    return create_response(response["Items"])


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)

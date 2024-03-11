import json
from boto3 import client
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics

tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")
create_response = lambda message: {"message": message}
client_lambda = client("lambda")


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    payload_to_orchestrator: dict = {
        "products_service": True,
        "describe_services": True,
    }
    logger.info("Making execution to orchestrator")
    response_of_orchestrator: dict = client_lambda.invoke(
        FunctionName="LAMBDA_PRAGMA_ASSESS_ORCHESTRATOR_USERS",
        LogType="Tail",
        Payload=bytes(json.dumps(payload_to_orchestrator), "utf-8"),
    )
    return create_response(response_of_orchestrator["Payload"].read())

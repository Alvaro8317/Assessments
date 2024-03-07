from typing import Union
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics

tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")
create_response = lambda message, can_create_saving_accounts: {
    "message": message,
    "canCreateASavingAccounts": can_create_saving_accounts,
}


def create_saving_accounts() -> dict:
    pass


def validate_requirements(age: int, country: str) -> bool:
    if age >= 18 and country == "COL":
        return True
    return False


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    logger.info(event)
    if validate_requirements(age=event["age"], country=event["country"]):
        return create_response("Can create a saving accounts", True)
    return create_response("Can not create a saving accounts", False)

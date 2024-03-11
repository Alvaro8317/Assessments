from typing import Union
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit
from database import UserClass
from models import OperationClient
tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")
create_response = lambda message: {"message": message}

@tracer.capture_method
def create_user(body) -> dict:
    code: Union[str, int] = body["code"]
    if UserClass.validate_user(code):
        return create_response(f"User with code: {code} already exists")
    metrics.add_metric(name="CreateUserInvocation", unit=MetricUnit.Count, value=1)
    response_dynamo = UserClass.create_user(event=body)
    logger.info(response_dynamo)
    return create_response(f"User created successfully: {body["name"]}")


def validate(id_user: Union[int, str]) -> dict:
    metrics.add_metric(name="ValidateUserInvocation", unit=MetricUnit.Count, value=1)
    if UserClass.validate_user(id_user=id_user):
        return create_response(f"The user with ID {id_user} exists already")
    return create_response(f"The user with ID {id_user} does not exists in our database")
    

@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    client = OperationClient(
        id=event.get("id", None),
        complete_name=event.get("complete_name", None),
        password=event.get("password", None),
        age=event.get("age", None),
        city=event.get("city", None),
        country=event.get("country", None),
        incomes=event.get("incomes", None),
        operation=event.get("operation", None),
        )

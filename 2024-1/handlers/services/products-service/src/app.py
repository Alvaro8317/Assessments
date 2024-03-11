from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics
from persistence import ProductPersistence

tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")
create_response = lambda message: {"message": message}


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    if "describe_services" in event:
        return create_response(ProductPersistence.get_available_products())

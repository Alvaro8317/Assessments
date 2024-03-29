import json
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics
from persistence import UserPersistence
from utils import generate_comment_of_ia
tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")
create_response = lambda message: {"message": message}


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    client = UserPersistence(
        id=event.get("id", ""),
        complete_name=event.get("complete_name", ""),
        password=event.get("password", ""),
        age=event.get("age", ""),
        city=event.get("city", ""),
        country=event.get("country", ""),
        incomes=event.get("incomes", ""),
    )
    if event["operation"] == "create":
        if client.validate_if_exists_user_with_that_id():
            return create_response("The user exists already")
        client.create_user()
        return create_response("User created successfully")
    if event["operation"] == "update":
        if not client.validate_if_exists_user_with_that_id():
            return create_response(
                "The user does not exists already, please create it first"
            )
        client.update_user()
        return create_response("User updated successfully")
    if event["operation"] == "validate":
        exists_user = client.validate_if_exists_user_with_that_id(
            set_data_of_database_to_instance=True
        )
        if not exists_user:
            return create_response(
                "The user does not exists already, please create it first"
            )

        result_domain_validations = client.validate_profile_of_user()
        comments = generate_comment_of_ia(result_domain_validations)
        comments_in_json = json.loads(comments)
        message_to_return = {
            "result_validations": result_domain_validations,
            "comments": comments_in_json["comments_of_ia"],
        }
        return create_response(message_to_return)
    return create_response("Operation not supported")

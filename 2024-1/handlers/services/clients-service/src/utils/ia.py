import json
from boto3 import client
from aws_lambda_powertools import Logger

logger = Logger()
client_lambda = client("lambda")
training = "Eres un asistente bancario que trabaja para AlgBank, a partir de este momento recibirás resultados de si alguien es apto para un producto o no y en base a estos resultados, genera una recomendación por favor, todo está en peso colombiano"


def generate_comment_of_ia(result_validations):
    payload_to_ia: dict = {
        "training": training,
        "result_validations": result_validations,
    }
    client_lambda.invoke(
        FunctionName="LAMBDA_PRAGMA_ASSESS_HELPER_IA",
        LogType="Tail",
        Payload=bytes(json.dumps(payload_to_ia), "utf-8"),
    )

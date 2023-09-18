import json
import base64
import boto3

client_kms = boto3.client('kms', region_name='us-east-1')
client_sns = boto3.client('sns')
client_sqs = boto3.client('sqs')
arn_of_sns = "arn:aws:sns:us-east-1:648254270796:SALUDPLUS"
arn_of_kms = "arn:aws:kms:us-east-1:648254270796:key/7c020ad4-1831-4ace-b0d6-baf7f490e147"
arn_of_sqs = "https://sqs.us-east-1.amazonaws.com/648254270796/SALUDPLUS"


def decode_url(url):
    return decrypt_url(base64.b64decode(url))


def decrypt_url(url_in_binary: bytes):
    return client_kms.decrypt(CiphertextBlob=url_in_binary,
                              KeyId=arn_of_kms, EncryptionAlgorithm='RSAES_OAEP_SHA_256')


def lambda_handler(event, context):
    body = json.loads(event['body'])
    cipher_url = decode_url(body['URL'])
    decrypted_url = cipher_url['Plaintext'].decode('utf-8')
    patient = body['patient']
    message_of_sns = """Estimado equipo de SALUDPLUS,
    
    Nos complace anunciar que hemos recibido una nueva fórmula médica que mejorará nuestros tratamientos. Encontrarán la fórmula médica del paciente {} en el siguiente enlace: {}. Ha quedado en la lista de espera para medicamentos que no han sido preparados aún.
    
    Si desean obtener más información o tienen alguna pregunta, no duden en ponerse en contacto con nuestro equipo médico o el departamento de recursos humanos.
    Gracias por su compromiso con la excelencia en la atención médica que ofrecemos en SALUDPLUS. Continuaremos trabajando juntos para proporcionar a nuestros pacientes el mejor cuidado posible.
    """.format(patient, decrypted_url)
    message_of_sqs = json.dumps({"Patient": patient, "URL": decrypted_url})
    bad_response = {
        'statusCode': 500,
        'body': {"message": "Something went wrong, please try again later"}
    }
    if not send_messages_to_sqs(message_to_send=message_of_sqs):
        return bad_response
    if not publish_in_sns(message=message_of_sns):
        return bad_response
    return {
        'statusCode': 200,
        'body': {"message": "Received successfully"}
    }


def publish_in_sns(message):
    try:
        response = client_sns.publish(
            TopicArn=arn_of_sns,
            Message=message,
            Subject="Nueva formula médica recibida"
        )
        print(response)
        return True
    except Exception as e:
        print(f"Something went wrong, details: {e}")
        return False


def send_messages_to_sqs(message_to_send: str):
    try:
        response = client_sqs.send_message(
            QueueUrl=arn_of_sqs,
            MessageBody=message_to_send,
            DelaySeconds=0)
        return True
    except Exception as e:
        print(f"SQS not available, details: {e}")
        return False

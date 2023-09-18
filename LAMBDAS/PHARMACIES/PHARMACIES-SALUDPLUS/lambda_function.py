import json
import base64
import boto3

client = boto3.client('kms', region_name='us-east-1')
key_id = 'arn:aws:kms:us-east-1:648254270796:key/7c020ad4-1831-4ace-b0d6-baf7f490e147'


def decode_url(url):
    return decrypt_url(base64.b64decode(url))


def decrypt_url(url_in_binary: bytes):
    return client.decrypt(CiphertextBlob=url_in_binary,
                          KeyId=key_id, EncryptionAlgorithm='RSAES_OAEP_SHA_256')
 


def lambda_handler(event, context):
    # TODO implement
    unescaped_url = (event['body'].replace("\\","")) + '"' + "}"
    cipher_url = json.loads(unescaped_url)
    print(decode_url(cipher_url['URL']))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


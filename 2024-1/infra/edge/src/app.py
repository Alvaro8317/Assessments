import Crypto
import base64
import json
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# PEM-formatted RSA public key copied over from AWS KMS or your own public key.
RSA_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAttD7+bXIgYUvR9k/gd7B
HA0k1aBXK4ujNWL2Sy1WEkPTR5ah5QlnWiNez0eKkYBENuj+CFUlXpxYIVWWawCf
YtQBOD9FyJo9WrPV/pEADupH3RyR+i2SJ0zTJ3UrXbDkxtv8kChGzLBCHt0sHLsA
TMlIcT3sQJxPIGdGL4871UHWTtTwZfe+O4vkCTtHLwxAlRUkECY4kdfyec1y0Zrf
K04l76i3Fys2Op//efbHUyGtqsyoWZ1hsl4kulZ1nXemPC6mE0RrMldcJL8w+R3e
nCgOvV1E/UurS1lQYit5zsoQoFjJOxeilyCFBTTyR7VCj50xhNLIcU2EBbB8TZFX
dQIDAQAB
-----END PUBLIC KEY-----"""
RSA_PUBLIC_KEY_OBJ = RSA.importKey(RSA_PUBLIC_KEY)
RSA_CIPHER_OBJ = PKCS1_OAEP.new(RSA_PUBLIC_KEY_OBJ, Crypto.Hash.SHA256)

PII_SENSITIVE_FIELD_NAMES = ["password", "authentication", "pwd"]

CIPHERTEXT_PREFIX = "#01#"
CIPHERTEXT_SUFFIX = "#10#"


# def lambda_handler(event, context):
#     http_request = event["Records"][0]["cf"]["request"]
#     body = http_request["body"]
#     print(body)
#     mod_body: dict = json.loads(http_request["body"])
#     if "password" in mod_body:
#         ciphertext = RSA_CIPHER_OBJ.encrypt(bytes(mod_body["password"], "utf-8"))
#         ciphertext_b64 = base64.b64encode(ciphertext).decode()
#         mod_body["password"] = CIPHERTEXT_PREFIX + ciphertext_b64 + CIPHERTEXT_SUFFIX
#     body["action"] = "replace"
#     body["encoding"] = "text"
#     body["data"] = mod_body
#     return http_request


def lambda_handler(event, context):
    http_request = event['Records'][0]['cf']['request']
    body = http_request['body']
    org_body = base64.b64decode(body['data'])
    mod_body = protect_sensitive_fields_json(org_body)
    body['action'] = 'replace'
    body['encoding'] = 'text'
    body['data'] = mod_body
    return http_request


def protect_sensitive_fields_json(body):
    person_list = json.loads(body.decode("utf-8"))
    for person_data in person_list:
        for field_name in PII_SENSITIVE_FIELD_NAMES:
            if field_name not in person_data:
                continue
            plaintext = person_data[field_name]
            ciphertext = RSA_CIPHER_OBJ.encrypt(bytes(plaintext, 'utf-8'))
            ciphertext_b64 = base64.b64encode(ciphertext).decode()
            person_data[field_name] = CIPHERTEXT_PREFIX + ciphertext_b64 + CIPHERTEXT_SUFFIX 
    return json.dumps(person_list)
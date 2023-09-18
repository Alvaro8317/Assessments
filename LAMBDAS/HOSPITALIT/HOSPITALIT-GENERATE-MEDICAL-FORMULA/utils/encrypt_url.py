import base64

def encrypt_url(client_boto3, url: str):
    arn_key = 'arn:aws:kms:us-east-1:648254270796:key/7c020ad4-1831-4ace-b0d6-baf7f490e147'
    url_in_binary = url.encode('utf-8')
    print(url_in_binary)
    response = client_boto3.encrypt(
        KeyId=arn_key, Plaintext=url_in_binary, EncryptionAlgorithm='RSAES_OAEP_SHA_256')
    return response['CiphertextBlob']

def encode_url(url: bytes):
    return base64.b64encode(url)
import requests
response = requests.post(
    'https://v3lrl256vt4fnktuqflj5ff2py0jmmxk.lambda-url.us-east-1.on.aws/', json={"payload": "Test"})
print(response.text)

aws dynamodb put-item --table-name Products --item "{\"CodeService\": {\"N\": \"1\"}, \"NameService\": {\"S\": \"Cuentas de ahorros\"}}" --region us-east-1 --output json
aws dynamodb put-item --table-name Products --item "{\"CodeService\": {\"N\": \"2\"}, \"NameService\": {\"S\": \"Tarjeta débito\"}}" --region us-east-1 --output json
aws dynamodb put-item --table-name Products --item "{\"CodeService\": {\"N\": \"3\"}, \"NameService\": {\"S\": \"Tarjeta crédito\"}}" --region us-east-1 --output json
aws dynamodb put-item --table-name Products --item "{\"CodeService\": {\"N\": \"4\"}, \"NameService\": {\"S\": \"Seguro\"}}" --region us-east-1 --output json
aws dynamodb put-item --table-name Products --item "{\"CodeService\": {\"N\": \"5\"}, \"NameService\": {\"S\": \"Inversiones\"}}" --region us-east-1 --output json
aws dynamodb put-item --table-name Products --item "{\"CodeService\": {\"N\": \"6\"}, \"NameService\": {\"S\": \"Giros\"}}" --region us-east-1 --output json
aws dynamodb put-item --table-name Products --item "{\"CodeService\": {\"N\": \"7\"}, \"NameService\": {\"S\": \"Tarjeta amparada\"}}" --region us-east-1 --output json
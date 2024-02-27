from database import Connection
connection = Connection(
    {"db_user": "HOSPITALITO", "db_password": "HOSPITALITO"}, print_uri=True)
print(type(connection.get_emr_user('6507c087a05456f191678d87')['patient']['name']))
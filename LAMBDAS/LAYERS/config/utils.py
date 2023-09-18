from dotenv import load_dotenv
import os


class Configuration:
    def __init__(self, show_variables: bool = False) -> None:
        pass

    def assign_variable_environments(self, print_variables: bool = False):
        load_dotenv()
        if (print_variables):
            print(os.getenv('DB_USER'))
            print(os.getenv('DB_PASSWORD'))
        return {
            'db_user': os.getenv('DB_USER'),
            'db_password': os.getenv('DB_PASSWORD'),
        }

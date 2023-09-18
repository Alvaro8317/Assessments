from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from .crud_enum import CRUD
from datetime import datetime
import os


class Connection:
    uri = f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@myatlasclusteredu.upe6arg.mongodb.net/?retryWrites=true&w=majority"
    variables = {}
    client = None
    db = None
    collection = None

    def __init__(self, env_variables: dict, print_uri: bool = False) -> None:
        self.uri = f"mongodb+srv://{env_variables['db_user']}:{env_variables['db_password']}@myatlasclusteredu.upe6arg.mongodb.net/?retryWrites=true&w=majority"
        if (print_uri):
            print(self.uri)
        self.connect_to_the_database()

    def connect_to_the_database(self):
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client['hospitalito']
        try:
            self.client.admin.command('ping')
            print("Conected successfully to the database")
        except Exception as e:
            print(e)

    def create_emr_user(self, user: dict):
        self._use_users_collection()
        user['datetimeCreated'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return self._crud_for_users(option=CRUD.CREATE, user=user)

    def get_emr_user(self, id: str):
        self._use_users_collection()
        print(id)
        return self._crud_for_users(option=CRUD.READ, id=id)

    def update_with_treatment_plan(self, id, new_diagnosis, new_treatment):
        self._use_users_collection()
        if (self._check_user_exists(id) == False):
            return 'User not found'
        new_diagnosis['date'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        diagnosis = self._get_a_diagnosis_or_treatments_of_user(
            id=id, property='diagnosis')
        diagnosis.append(new_diagnosis)
        treatment = self._get_a_diagnosis_or_treatments_of_user(
                id=id, property='treatments')
        if (new_treatment != None):
            treatment.append(new_treatment)
        values_to_update = {
            "$set": {"treatments": treatment, "diagnosis": diagnosis}}
        self._crud_for_users(CRUD.UPDATE, id=id, values_to_update=values_to_update)

    def _use_users_collection(self):
        self.collection = self.db['users']

    def _crud_for_users(self, option: CRUD, user: dict = None, id: str = None, values_to_update: dict = None, print_message: bool = False):
        response = 'Unexpected error, please check the logs'
        try:
            match option:
                case CRUD.CREATE:
                    if (print_message): 
                        print("Creating user")
                    return self.collection.insert_one(user).inserted_id
                case CRUD.READ:
                    if (print_message): 
                        print("Getting user")
                    user = self.collection.find_one({"_id": ObjectId(id)})
                    user['_id'] = str(user['_id'])
                    return user
                case CRUD.UPDATE:
                    try:
                        if (print_message): 
                            print('Updating user')
                        response = self.collection.update_one({"_id": ObjectId(id)}, values_to_update)
                        return True
                    except Exception as e:
                        print(e)
                    
        except Exception as e:
            print(e)
        return response

    def _check_user_exists(self, id):
        user = self.collection.find_one({"_id": ObjectId(id)})
        if (user == None):
            return False
        return user

    def _get_a_diagnosis_or_treatments_of_user(self, id, property: str) -> list:
        complete_user = self._crud_for_users(option=CRUD.READ, id=id)
        return complete_user[property]

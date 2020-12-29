import json
import os
import time
import threading
from sys import getsizeof

global_lock = threading.Lock()


class JsonFileOperation(object):
    def __init__(self, filepath=None):
        self.filepath = filepath
        if not filepath:
            self.filepath = './default.json'
            if not os.path.isfile(self.filepath):
                with open(self.filepath, 'w') as file:
                    json.dump({}, file)
        self.validate_file(self.filepath)

    '''
	The function validate_file valids both filepath and filesize and raises an
	exception when the path is invalid or filesize exceeds 1GB = 1073741824 bytes.
	'''

    def validate_file(self, filepath):
        if not os.path.exists(filepath):
            raise Exception("Invalid file path")
        if os.stat(filepath).st_size > 1073741824:
            raise Exception("File size exceeded 1GB")

    '''
	The function validate_key valids key length and raises an
	exception when the key length exceeds 32 characters.
	'''

    def validate_key(self, key):
        if len(key) > 32:
            raise Exception("Max key length allowed is 32 chars")
        if not key.isalpha():
            raise Exception(
                "Key must contain only alphabets and no special characters or numbers")

    '''
	The function validate_value valids value size and raises an
	exception when the value size exceeds 16 KB = 16000 bytes.
	'''

    def validate_value(self, value):
        if getsizeof(value) > 16000:
            raise Exception("Max value size allowed is 16KB")

    '''
	The function validate_value valids value size and raises an
	exception when the value size exceeds 16 KB = 16000 bytes.
	'''

    def validate_jsonobj(self, json_obj):
        if len(json.dumps(json_obj)) > 1073741824:
            raise Exception("File size exceeds 1GB")

    '''
	The function read_file is responsible for returning a json object from the loaded file.
	'''

    def read_file(self):
        file = open(self.filepath, "r")
        return json.load(file)

    '''
	The function create_data is responsible for creating JSON data, for the given filepath, key, value and an optional timeout as
	arguments and raises an exception, when key already exists.
	'''

    def create_data(self, key, value, ttl=None):
        while global_lock.locked():
            continue
        global_lock.acquire()
        self.validate_key(key)
        self.validate_value(value)
        self.validate_file(self.filepath)
        json_obj = self.read_file()

        if key in json_obj:
            raise Exception("Key already exists")

        json_obj[key] = {}
        with open(self.filepath, "w") as file:
            json_obj[key]['value'] = value
            if ttl:
                json_obj[key]['ttl'] = time.time() + ttl
            self.validate_jsonobj(json_obj)
            json.dump(json_obj, file)
        global_lock.release()
        return "data_created"

    '''
	The function read_data is responsible for reading the JSON data, for the provided key,if
	key is not found raises key not found as an exception.
	'''

    def read_data(self, key):
        self.validate_key(key)
        json_obj = self.read_file()

        if key not in json_obj:
            raise Exception("Key does not exists")

        value = json_obj[key]
        ttl = value.get('ttl', None)
        if ttl and not time.time() < ttl:
            del json_obj[key]
            raise Exception("key has expired")
        return value['value']

    '''
	The function delete_data is responsible for deleting the JSON data, for the provided key, 
	if key is not found raises key not found as an exception.
	'''

    def delete_data(self, key):
        while global_lock.locked():
            continue
        global_lock.acquire()
        self.validate_key(key)
        json_obj = self.read_file()

        if key not in json_obj:
            raise Exception("Key does not exists")

        value = json_obj[key]
        ttl = value.get('ttl', None)
        if ttl and not time.time() < ttl:
            raise Exception("key has expired")

        del json_obj[key]
        with open(self.filepath, "w") as file:
            json.dump(json_obj, file)
        global_lock.release()
        return "data_deleted"

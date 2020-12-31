import json
import os
import time
import threading
from .jsonfile_helper import HelperValidator

# helper_obj is used access methods from HelpValidator class
helper_obj = HelperValidator()

# global_lock is an variable assigned to access Lock() from threading.
global_lock = threading.Lock()

global filename

# default filename when filename is not specified by the user.
filename = './default.json'

class JsonFileOperation(object):
    '''
    The class JsonFileOperation is responsible for executing functions 
    like create_data, read_data, delete_data under thread-safe 
    conditions.
    '''
    def __init__(self, filepath=None):
        self.filepath = filepath
        if not filepath:
            self.filepath = filename
            if not os.path.isfile(self.filepath):
                with open(self.filepath, 'w') as file:
                    json.dump({}, file)
        helper_obj.validate_file(self.filepath)

    def create_data(self, key, value, ttl=None):
        '''
        The function create_data is responsible for creating JSON data, 
        for the given filepath, key, value and an optional timeout as
        arguments and raises an exception, when key already exists.
        '''
        while global_lock.locked():
            continue
        global_lock.acquire()
        helper_obj.validate_key(key)
        helper_obj.validate_value(value)
        helper_obj.validate_file(self.filepath)
        json_obj = helper_obj.read_file(self.filepath)

        if key in json_obj:
            raise Exception("Key already exists")

        json_obj[key] = {}
        with open(self.filepath, "w") as file:
            json_obj[key]['value'] = value
            if ttl:
                json_obj[key]['ttl'] = time.time() + ttl
            helper_obj.validate_jsonobj(json_obj)
            json.dump(json_obj, file)
        global_lock.release()
        return "data_created"
    
    
    def read_data(self, key):
        '''
        The function read_data is responsible for reading the JSON data, 
        for the provided key,if key is not found raises key not found as 
        an exception.
        '''
        helper_obj.validate_key(key)
        json_obj = helper_obj.read_file(self.filepath)

        if key not in json_obj:
            raise Exception("Key does not exists")

        value = json_obj[key]
        ttl = value.get('ttl', None)
        if ttl and not time.time() < ttl:
            del json_obj[key]
            raise Exception("key has expired")
        return value.get('value')

    

    def delete_data(self, key):
        '''
        The function delete_data is responsible for deleting the JSON data, 
        for the provided key, if key is not found raises key not found as 
        an exception.
        '''
        while global_lock.locked():
            continue
        global_lock.acquire()
        helper_obj.validate_key(key)
        json_obj = helper_obj.read_file(self.filepath)

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
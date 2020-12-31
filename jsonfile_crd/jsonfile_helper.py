from sys import getsizeof
import json
import os

# Constants 1GB = 1073741824 bytes, 16KB = 16000 bytes, keylength = 32 bytes.
MAX_FILESIZE = 1073741824
MAX_KEYLENGTH = 32
MAX_VALUESIZE = 16000

class HelperValidator:
    '''
    The class HelperValidator is responsible for validating filepath, 
    filesize, key, value, json_obj and loading a file.
    '''

    def validate_file(self,filepath):
        '''
        The function validate_file validates both filepath and filesize and raises an
        exception when the path is invalid or filesize exceeds MAX_FILESIZE.
        '''
        if not os.path.exists(filepath):
            raise Exception("Invalid file path")
        if os.stat(filepath).st_size > MAX_FILESIZE:
            raise Exception("File size exceeded 1GB")

    def validate_key(self,key):
        '''
        The function validate_key validates key length and raises an
        exception when the key length exceeds 32 bytes.
        '''
        if len(key) > MAX_KEYLENGTH:
            raise Exception("Max key length allowed is 32 bytes")
        if not key.isalpha():
            raise Exception("Key must contain only alphabets and no special characters or numbers")

    def validate_value(self,value):
        '''
        The function validate_value validates value size and raises an
        exception when the value size exceeds 16000 bytes.
        '''
        if getsizeof(value) > MAX_VALUESIZE:
            raise Exception("Max value size allowed is 16KB")
    
   

    def validate_jsonobj(self,json_obj):
        '''
        The function validate_jsonobj validates object that is returned 
        and raises an exception when the object size exceeds MAXFILESIZE.
        '''
        if len(json.dumps(json_obj)) > MAX_FILESIZE:
            raise Exception("File size exceeds 1GB")
    
    

    def read_file(self,filepath):
        '''
        The function read_file is responsible for returning a json object 
        from the loaded file.
        '''
        file = open(filepath, "r")
        return json.load(file)   
import json,os,time
from sys import getsizeof

class JSONCRD(object):
    def __init__(self,file_path = None,output_file = None):
        if file_path and output_file is None:
            cur_dir = os.getcwd()
            output_file = '/DB_store.json'
            self.buildpath = cur_dir + output_file
            print(self.buildpath)
            try:
                file = open(self.buildpath,'w')
                file.write('{}')
                file.close()
            except:
                raise Exception("Error in file creation")
        elif len(output_file) > 0 and file_path is None:
            cur_dir = os.getcwd()
            output_file = output_file
            self.buildpath = cur_dir+ '/' +output_file
            print(self.buildpath)
            try:
                file = open(self.buildpath,'w')
                file.write('{}')
                file.close()
            except:
                raise Exception("Error in file creation")
        else:
            cur_dir = file_path
            output_file = output_file
            self.buildpath = cur_dir + output_file
            if not os.path.exists(self.buildpath):raise Exception("Invalid file path")


    '''
    The function validate_file valids both filepath and filesize and raises an 
    exception when the path is invalid or filesize exceeds 1GB.
    '''

    def validate_file(self,file_path):
        if not os.path.exists(file_path):raise Exception("Invalid file path")
        if os.stat(file_path).st_size > 1073741824:raise Exception("File size exceeded 1GB")

    '''
    The function validate_key valids key length and raises an 
    exception when the key length exceeds 32 characters.
    '''

    def validate_key(self,key):
        if len(key) > 32:raise Exception("Max key length allowed is 32 chars")
        if not key.isalpha():raise Exception("Key must contain only alphabets and no special characters or numbers")

    '''
    The function validate_value valids value size and raises an 
    exception when the value size exceeds 16 kilobytes.
    '''

    def validate_value(self,value):
        if getsizeof(value) > 16000:raise Exception("Max value size allowed is 16KB")

    '''
    The function create_data is responsible for creating JSON data, for the given filepath, key, value and an optional timeout as 
    arguments and raises an exception, when key already exists. 
    '''

    def create_data(self,timeout=0):
        key = input("Enter the key: ").strip()
        value = input("Enter the value: ").strip()
        timeout = int(input("Add a timeout in Seconds(optional): "))
        self.validate_key(key)
        self.validate_value(value)
        file = open(self.buildpath,"r")
        obj = json.load(file)
        file.close()
        if key in obj:
            raise Exception("Key already exists")
        else:
            if timeout == 0:
                l = [value,timeout]
                print(False)
            else:
                l=[value,time.time()+timeout]
                print(True)
            obj[key] = l
            file = open(self.buildpath,"w")
            json.dump(obj,file)
            file.close()
            return "data_created"

    '''
    The function read_data is responsible for reading the JSON data, for the provided key,if 
    key is not found raises key not found as an exception.
    '''

    def read_data(self):
        self.validate_file(self.buildpath)
        key = input("Enter the key: ")
        self.validate_key(key)
        file = open(self.buildpath,"r")
        obj = json.load(file)
        file.close()
        if key in obj:
            b = obj[key]
            if b[1] != 0:
                if time.time() < b[1]: 
                    buildstr=str(key)+":"+str(b[0])
                    return buildstr
                else:
                    raise Exception("Time-to-live of",key,"has expired")
            else:
                buildstr = str(key)+":"+str(b[0])
                return buildstr
        else:
            raise Exception("Key does not exists")

    '''
    The function delete_data is responsible for deleting the JSON data, for the provided key, 
    if key is not found raises key not found as an exception.
    '''

    def delete_data(self):
        self.validate_file(self.buildpath)
        key = input("Enter the key: ")
        self.validate_key(key)
        file = open(self.buildpath,"r")
        obj = json.load(file)
        file.close()
        if key in obj:
            b = obj[key]
            if b[1] !=0:
                if time.time() < b[1]:
                    del obj[key]
                    file = open(self.buildpath,"w")
                    json.dump(obj,file)
                    file.close()
                    return "%s data_deleted"%(key)
                else:
                    return "%s key expired cannot be deleted"%(key)
            else:
                del obj[key]
                file = open(self.buildpath,"w")
                json.dump(obj,file)
                file.close()
                return "%s data_deleted"%(key)
        else:
            raise Exception("Key does not exists")
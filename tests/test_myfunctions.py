#old tests
from mypythonlib import myfunctions

#file_path = '/Users/jagan/desktop/testing/DB_store.json'

#key = "hello"
#value = "world"

def test_create():
    assert myfunctions.create_data(file_path,key,value) == "data_created"

def test_read():
    assert myfunctions.read_data(file_path,key) == "data_read"
    
def test_delete():
    assert myfunctions.delete_data(file_path,key) == "data_deleted"
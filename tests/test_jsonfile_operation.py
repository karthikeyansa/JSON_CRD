from jsonfile_crd.jsonfile_operation import JsonFileOperation

obj = JsonFileOperation()

'''
The function test_JsonFileOperation with key, value and ttl as arguments 
returns "data_created", "key", "data_deleted".
'''

key = "car"
value = "ola"
ttl = 120


def test_JsonFileOperation():
    assert obj.create_data(key, value, ttl) == "data_created"
    assert obj.read_data(key) == value
    assert obj.delete_data(key) == "data_deleted"

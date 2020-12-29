from jsonfile_crd.jsonfile_operation import JsonFileOperation

obj = JsonFileOperation()

'''
Testing create function with key, value and ttl as arguments.
'''


def test_create():
    assert obj.create_data("car", "ola", 120) == "data_created"


'''
Testing read function with key as argument.
'''


def test_read():
    assert obj.read_data("car") == "ola"


'''
Testing delete function with key arguments.
'''


def test_delete():
    assert obj.delete_data("car") == "data_deleted"

from jsonfile_crd.jsonfile_operation import JsonFileOperation
import threading
from time import sleep

#object creation to access JsonFileOperation(filepath), filepath is specified by the user
jsonfile_obj = JsonFileOperation()

def mycreateThread(args):
    '''
    This function is responsible to call create_data from JsonFileOperation class.
    '''
    key = "data"+chr(97+args)
    value = "abcd"+chr(97+args)
    ttl = 200
    jsonfile_obj.create_data(key, value, ttl)


def myreadThread(args):
    '''
    This function is responsible to call read_data 
    from JsonFileOperation class.
    '''
    key = "data"+chr(97+args)
    jsonfile_obj.read_data(key)


def mydeleteThread(args):
    '''
    This function is responsible to call delete_data 
    from JsonFileOperation class.
    '''
    key = "data"+chr(97+args)
    jsonfile_obj.delete_data(key)

create_thread = []
read_thread = []
delete_thread = []


for i in range(5):
    '''
    This loop creates and appends threads for performing 
    create, read, delete operations.
    '''
    ct = threading.Thread(target= mycreateThread, args=[i,])
    rt = threading.Thread(target= myreadThread, args=[i,])
    dt = threading.Thread(target= mydeleteThread, args=[i,])
    create_thread.append(ct)
    read_thread.append(rt)
    delete_thread.append(dt)


for c,r,d in zip(create_thread,read_thread,delete_thread):
    '''
    All Threads are started from create_thread, read_thread, delete_thread, 
    with a delay of 1 seconds. 
    '''
    c.start()
    sleep(1)
    r.start()
    sleep(1)
    d.start()
    sleep(1)

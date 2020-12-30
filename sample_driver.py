from jsonfile_crd.jsonfile_operation import JsonFileOperation
import threading
from time import sleep

#object creation to access JsonFileOperation
obj = JsonFileOperation()

'''
This function is responsible to call create_data from JsonFileOperation class.
'''

def mycreateThread(args):
    key = "data"+chr(97+args)
    value = "abcd"+chr(97+args)
    ttl = 200
    obj.create_data(key, value, ttl)

'''
This function is responsible to call read_data from JsonFileOperation class.
'''

def myreadThread(args):
    key = "data"+chr(97+args)
    obj.read_data(key)

'''
This function is responsible to call delete_data from JsonFileOperation class.
'''

def mydeleteThread(args):
    key = "data"+chr(97+args)
    obj.delete_data(key)

create_thread = []
read_thread = []
delete_thread = []

'''
This loop creates and appends threads for performing create, read, delete operations.
'''
for i in range(26):
    ct = threading.Thread(target= mycreateThread, args=[i,])
    rt = threading.Thread(target= myreadThread, args=[i,])
    dt = threading.Thread(target= mydeleteThread, args=[i,])
    create_thread.append(ct)
    read_thread.append(rt)
    delete_thread.append(dt)

# All Threads are started from create_thread, read_thread, delete_thread, with a delay of 0.5 seconds. 
for c,r,d in zip(create_thread,read_thread,delete_thread):
    c.start()
    sleep(0.5)
    r.start()
    sleep(0.5)
    d.start()
    sleep(0.5)

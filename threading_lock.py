import threading

global_lock = threading.Lock()

def write_to_file():
    while global_lock.locked():
        continue

    global_lock.acquire()

    with open("thread_writes", "a+") as file:
        file.write(str(threading.get_ident()))
        file.write("\n")
        file.close()

    global_lock.release()

# Create a 200 threads, invoke write_to_file() through each of them,
# and 
threads = []
for i in range(1, 20):
    t = threading.Thread(target=write_to_file)
    threads.append(t)
    t.start()
[thread.join() for thread in threads]

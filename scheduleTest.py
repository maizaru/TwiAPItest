import time,threading

def worker():
    print(time.time())
    time.sleep(8)

def scheduler(interval,f,count,wait=True):
    base_time = time.time()
    next_time = 0
    for i in range(count):
        t = threading.Thread(target = f)
        t.start()
        if wait:
            t.join()
        time.sleep(interval)
import threading
import time
import random

book = "AAA"
rw_mutex = threading.Lock() 
mutex = threading.Lock()    
read_count = 0
count_w = 0

def writer():
    global book, count_w
    for _ in range(2):
        rw_mutex.acquire()
        book = f"HEHEHE {count_w}"
        count_w += 1
        print(f"Writer sửa: {book}")
        rw_mutex.release()
        time.sleep(random.uniform(0.5, 1))

def reader(i):
    global read_count
    for _ in range(3):
        mutex.acquire()
        read_count += 1
        if read_count == 1: rw_mutex.acquire()
        mutex.release()
        
        print(f"Reader {i} đọc: {book}")
        time.sleep(1)
        
        mutex.acquire()
        read_count -= 1
        if read_count == 0: rw_mutex.release()
        mutex.release()
        time.sleep(random.uniform(0.1, 0.3))

readers = [threading.Thread(target=reader, args=(i,)) for i in range(2)]
writers = [threading.Thread(target=writer)]

for r in readers: r.start()
for w in writers: w.start()
for r in readers: r.join()
for w in writers: w.join()

print("Done!")
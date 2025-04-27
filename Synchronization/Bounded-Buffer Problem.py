import threading
import time
import random

buffer = []
BUFFER_SIZE = 3

empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Lock()

def producer(producer_id):
    for i in range(5):
        print(f"Producer {producer_id} muốn thêm item, kiểm tra slot...")
        empty.acquire()
        with mutex:
            buffer.append("X")
            print(f"Producer {producer_id} thêm item, Buffer: {buffer}")
        full.release()
        time.sleep(random.uniform(0.1, 0.3))

def consumer(consumer_id):
    for _ in range(5):
        print(f"Consumer {consumer_id} muốn lấy item, kiểm tra buffer...")
        full.acquire()
        with mutex:
            item = buffer.pop(0)
            print(f"Consumer {consumer_id} lấy {item}, Buffer: {buffer}")
        empty.release()
        time.sleep(random.uniform(0.5, 0.8))

producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]

for p in producers:
    p.start()
for c in consumers:
    c.start()

for p in producers:
    p.join()
for c in consumers:
    c.join()

print("Done!")
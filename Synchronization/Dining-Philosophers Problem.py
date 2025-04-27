import threading
import time
import random

class DiningMonitor:
    def __init__(self):
        self.lock = threading.Lock()
        self.state = ["THINKING"] * 5
        self.cond = [threading.Condition(self.lock) for _ in range(5)]

    def pickup(self, i):
        with self.lock:
            self.state[i] = "HUNGRY"
            print(f"Philosopher {i} đói, muốn ăn...")
            self.test(i)
            if self.state[i] != "EATING":
                self.cond[i].wait()

    def putdown(self, i):
        with self.lock:
            self.state[i] = "THINKING"
            print(f"Philosopher {i} ăn xong, tiếp tục nghĩ...")
            self.test((i + 4) % 5)
            self.test((i + 1) % 5)

    def test(self, i):
        if (self.state[(i + 4) % 5] != "EATING" and 
            self.state[i] == "HUNGRY" and 
            self.state[(i + 1) % 5] != "EATING"):
            self.state[i] = "EATING"
            print(f"Philosopher {i} đang ăn...")
            self.cond[i].notify()

monitor = DiningMonitor()

def philosopher(i):
    for _ in range(3):
        print(f"Philosopher {i} đang nghĩ...")
        time.sleep(random.uniform(0.5, 1))
        monitor.pickup(i)
        time.sleep(random.uniform(0.5, 1))
        monitor.putdown(i)

philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(5)]

for p in philosophers: p.start()
for p in philosophers: p.join()

print("Done!")
from collections import deque

# Lớp Process với arrival_time
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid                  
        self.arrival_time = arrival_time  
        self.burst_time = burst_time      
        self.remaining_time = burst_time 

def mlfq(processes, quanta):
    queues = [deque(), deque(), deque()]  
    current_time = 0
    remaining_processes = processes.copy() 
    
    while any(queues) or remaining_processes:  
        for p in remaining_processes[:]:
            if p.arrival_time <= current_time:
                queues[0].append(p)
                remaining_processes.remove(p)
                print(f"Time {current_time}: P{p.pid} arrived and added to Queue 0")

        found = False
        for q in range(3):
            if queues[q]:
                found = True
                process = queues[q].popleft()  
                quantum = quanta[q] 
                run_time = min(quantum, process.remaining_time) 
                
                print(f"Time {current_time}: P{process.pid} (Queue {q}) runs for {run_time}")
                
                process.remaining_time -= run_time 
                current_time += run_time 
                
                if process.remaining_time > 0:
                    next_q = min(q + 1, 2)  
                    queues[next_q].append(process)
                    print(f"Time {current_time}: P{process.pid} moved to Queue {next_q}")
                else:
                    print(f"Time {current_time}: P{process.pid} completed")
                break  
        
        if not found and remaining_processes:
            current_time += 1
            print(f"Time {current_time}: No process ready")


if __name__ == "__main__":
    processes = [
        Process(1, 0, 10), 
        Process(2, 2, 4),
        Process(3, 4, 8), 
    ]
    
    quanta = [2, 4, 8]  
    
    print("Starting Simple MLFQ Simulation with Arrival Times...\n")
    mlfq(processes, quanta)
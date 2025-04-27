class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0
        self.start_time = -1  

def priority_with_round_robin(processes, time_quantum):
    processes.sort(key=lambda p: p.arrival_time)  
    queue = []  
    time = 0  
    index = 0  
    completed_processes = []

    while index < len(processes) or queue:
        while index < len(processes) and processes[index].arrival_time <= time:
            queue.append(processes[index])
            queue.sort(key=lambda p: p.priority)  
            index += 1

        if queue:
            process = queue.pop(0)
            if process.start_time == -1:
                process.start_time = time  

            execute_time = min(process.remaining_time, time_quantum)
            process.remaining_time -= execute_time
            time += execute_time

            while index < len(processes) and processes[index].arrival_time <= time:
                queue.append(processes[index])
                queue.sort(key=lambda p: p.priority)  
                index += 1

            if process.remaining_time > 0:
                queue.append(process)
                queue.sort(key=lambda p: p.priority)  
            else:
                process.completion_time = time  
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                completed_processes.append(process)
        else:
            time += 1  

    return completed_processes

def print_results(processes):
    print("PID\tArrival\tPriority\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.priority}\t\t{p.burst_time}\t\t{p.completion_time}\t\t{p.waiting_time}\t\t{p.turnaround_time}")

process_list = [
    Process(1, 0, 4, 3),
    Process(2, 1, 5, 2),
    Process(3, 2, 8, 2),
    Process(4, 3, 7, 1),
    Process(5, 4, 3, 3)
]

time_quantum = 2
scheduled_processes = priority_with_round_robin(process_list, time_quantum)
print_results(scheduled_processes)

def sjf_non_preemptive(processes):
    processes.sort(key=lambda x: x[1])
    
    n = len(processes)
    waiting_time = [0] * n 
    completion_time = [0] * n  
    turnaround_time = [0] * n 
    executed = [False] * n 
    
    current_time = 0
    completed = 0
    gantt = []
    
    while completed < n:
        ready_queue = []
        for i in range(n):
            if processes[i][1] <= current_time and not executed[i]:
                ready_queue.append((i, processes[i][2])) 
        
        if not ready_queue:
            current_time += 1
            continue
        
        ready_queue.sort(key=lambda x: x[1]) 
        process_idx = ready_queue[0][0]
        
        executed[process_idx] = True
        completion_time[process_idx] = current_time + processes[process_idx][2]
        turnaround_time[process_idx] = completion_time[process_idx] - processes[process_idx][1]
        waiting_time[process_idx] = turnaround_time[process_idx] - processes[process_idx][2]
        current_time = completion_time[process_idx]
        completed += 1
        gantt.append(f"P{processes[process_idx][0]}")
    
    print("\nBiểu đồ Gantt:")
    
    gantt_str = "  ".join([f"{x:^6}" for x in gantt])
    print(f"| {gantt_str} |")
    
    time_points = [0]
    for i in range(n):
        for j in range(n):
            if f"P{processes[j][0]}" == gantt[i]:
                temp_time = completion_time[j]
        time_points.append(temp_time)
    
    time_line = "  ".join([f"{t:^6}" for t in time_points])
    print(f"  {time_line}")
    
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    avg_waiting_time = sum(waiting_time) / n
    print(f"\nThời gian chờ trung bình (Average Waiting Time): {avg_waiting_time:.2f}")

processes = [
    (1, 0, 10),  
    (2, 1, 29),  
    (3, 2, 3),   
    (4, 0, 7),   
    (5, 3, 12)   
]

sjf_non_preemptive(processes)
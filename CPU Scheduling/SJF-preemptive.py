def sjf_preemptive(processes):
    processes.sort(key=lambda x: x[1])
    
    n = len(processes)
    waiting_time = [0] * n 
    completion_time = [0] * n  
    turnaround_time = [0] * n  
    remaining_time = [p[2] for p in processes]  
    executed = [False] * n  
    
    current_time = 0
    completed = 0
    gantt = []
    time_points = [0] 
    
    while completed < n:
        ready_queue = []
        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] > 0:
                ready_queue.append((i, remaining_time[i])) 
        
        if not ready_queue:
            current_time += 1
            gantt.append("Idle")
            time_points.append(current_time)
            continue
        
        ready_queue.sort(key=lambda x: x[1]) 
        process_idx = ready_queue[0][0]
        
        remaining_time[process_idx] -= 1
        gantt.append(f"P{processes[process_idx][0]}")
        current_time += 1
        time_points.append(current_time)
        
        if remaining_time[process_idx] == 0:
            completed += 1
            executed[process_idx] = True
            completion_time[process_idx] = current_time
            turnaround_time[process_idx] = completion_time[process_idx] - processes[process_idx][1]
            waiting_time[process_idx] = turnaround_time[process_idx] - processes[process_idx][2]
    
    print("\nBiểu đồ Gantt:")
    gantt_str = "  ".join([f"{x:^6}" for x in gantt])
    print(f"| {gantt_str} |")
    
    time_line = "  ".join([f"{t:^6}" for t in time_points])
    print(f"  {time_line}")
    
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    avg_waiting_time = sum(waiting_time) / n
    print(f"\nThời gian chờ trung bình (Average Waiting Time): {avg_waiting_time:.2f}")

processes = [
    (0, 3, 2),  
    (1, 2, 4),  
    (2, 0, 6), 
    (3, 1, 4),  
]

sjf_preemptive(processes)
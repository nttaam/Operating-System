def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])
    
    n = len(processes)
    waiting_time = [0] * n  
    completion_time = [0] * n  
    turnaround_time = [0] * n 
    
    current_time = 0
    gantt_segments = [] 
    time_points = [0]   
    
    for i in range(n):
        if current_time < processes[i][1]:
            current_time = processes[i][1]
            time_points.append(current_time)
            gantt_segments.append("Idle")

        gantt_segments.append(f"P{processes[i][0]}")
        completion_time[i] = current_time + processes[i][2]
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]
        current_time = completion_time[i]
        time_points.append(current_time)
    
    print("\nBiểu đồ Gantt:")
    gantt_str = "  ".join([f"{x:^6}" for x in gantt_segments])  
    print(f"| {gantt_str} |")
    
    time_line = "  ".join([f"{t:^6}" for t in time_points]) 
    print(f"  {time_line}")
    
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{completion_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    avg_waiting_time = sum(waiting_time) / n
    print(f"\nThời gian chờ trung bình (Average Waiting Time): {avg_waiting_time:.2f}")

processes = [
    (1, 1, 24),  
    (2, 0, 3),  
    (3, 2, 3)    
]

fcfs_scheduling(processes)
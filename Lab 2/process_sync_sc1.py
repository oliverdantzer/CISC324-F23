class Request:
    def __init__(self, id, processing_time):
        self.id = id
        self.processing_time = processing_time
        self.remaining_time = processing_time
        self.wait_time = 0

    # TODO: Add other necessary methods if required

def start_scheduling(requests, time_quantum,method):
    if method == 'robin':
        round_robin(requests, time_quantum)
    else:
        second(requests, time_quantum)

def round_robin(requests, time_quantum):
    queue = []
    turnaround = {}
    arrival_times = {} 
    elapsed_time = 0
    
    for req in requests:
        queue.append(req)
    
    while (len(queue)>0):
        req = queue.pop()
        if(req.remaining_time > time_quantum):
            req.remaining_time -= time_quantum
            elapsed_time+= time_quantum 
            if (req.id not in arrival_times):
                arrival_times[req.id] = elapsed_time
            queue.append(req)
        else:
            elapsed_time+=req.remaining_time
            req.remaining_time = 0
            turnaround[req.id] = elapsed_time - arrival_times[req.id]
            req.wait_time = turnaround[req.id] - req.processing_time
    
    for req in requests:
        print(f"Request ID: {req.id}, Waiting Time: {req.wait_time}, Turnaround Time: {turnaround[req.id]}")
        total_wait_time += req.wait_time
        total_turnaround_time += turnaround[req.id]
        #req.wait_time = 0
        #req.remaining_time = req.processing_time
    #print(f"Average Waiting Time: {total_wait_time/len(requests)}")
    #print(f"Average Turnaround Time: {total_turnaround_time/len(requests)}")


def second(requests, time_quantum):
    pass
    
    

def generate_random_requests(num_requests=20):
    import random
    
    # Generates a list of random client requests
    return [Request(i, random.randint(1, 10)) for i in range(num_requests)]

def main():
    #requests = generate_random_requests()

    requests_tc1 = [Request(0, 3), Request(1, 2), Request(2, 4), Request(3, 5), Request(4, 1)]
    requests_tc2 = [Request(0, 4), Request(1, 6), Request(2, 8), Request(3, 2), Request(4, 4)]

    print('\n**************Test case# 1**************\n')
    # Displaying generated requests
    for req in requests_tc1:
        print(f"Request ID: {req.id}, Processing Time: {req.processing_time}")

    time_quantum = 3  # You can adjust this value based on requirements
    start_scheduling(requests_tc1, time_quantum,"robin")


    print('\n**************Test case# 2**************\n')
    # Displaying generated requests
    for req in requests_tc2:
        print(f"Request ID: {req.id}, Processing Time: {req.processing_time}")

    time_quantum = 3  # You can adjust this value based on requirements
    start_scheduling(requests_tc2, time_quantum,"robin")

    # TODO: Calculate and display the average waiting time and average turnaround time

if __name__ == "__main__":
    main()

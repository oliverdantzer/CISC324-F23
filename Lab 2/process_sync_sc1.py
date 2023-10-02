class Request:
    def __init__(self, id, processing_time):
        self.id = id
        self.processing_time = processing_time
        self.remaining_time = processing_time
        self.wait_time = 0

    # TODO: Add other necessary methods if required

def start_scheduling(requests, time_quantum):
    # This function will handle the scheduling algorithm
    
    # TODO: Implement the scheduling algorithm
    # Hint: You might need a queue to keep track of requests
    
    pass

def first_come_first_serve(requests):
    # This function will handle the first come first serve algorithm
    waiting_time_sum = 0
    turnaround_time_sum = 0
    time = 0
    for request in requests:
        arrival_time = time
        time += request.processing_time
        burst_time = time - arrival_time
        waiting_time = time
        turnaround_time = waiting_time + burst_time
        waiting_time_sum += waiting_time
        turnaround_time_sum += turnaround_time
    #avg waiting time, avg turnaround time
    return waiting_time_sum / len(requests), turnaround_time_sum / len(requests)

    

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
    start_scheduling(requests_tc1, time_quantum)


    print('\n**************Test case# 2**************\n')
    # Displaying generated requests
    for req in requests_tc2:
        print(f"Request ID: {req.id}, Processing Time: {req.processing_time}")

    time_quantum = 3  # You can adjust this value based on requirements
    start_scheduling(requests_tc2, time_quantum)

    # TODO: Calculate and display the average waiting time and average turnaround time

if __name__ == "__main__":
    main()

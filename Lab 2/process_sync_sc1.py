class Request:
    def __init__(self, id, processing_time):
        self.id = id
        self.processing_time = processing_time
        self.remaining_time = processing_time
        self.wait_time = 0

    # TODO: Add other necessary methods if required

def start_scheduling(requests, time_quantum,arrivals):
    print("Round robin:")
    round_robin(requests, time_quantum,arrivals)


def round_robin(requests, time_quantum, arrivals):
    queue = []
    turnaround = {}
    elapsed_time = 0
    total_turnaround_time = 0
    total_wait_time = 0
    
    #add requests to queue
    for req in requests:
        queue.append(req)
    #sort queue by arrival time
    queue.sort(key=lambda x: arrivals[x.id])
    
    while (len(queue)>0):

        #check if request has arrived
        if (elapsed_time >= arrivals[queue[0].id]):
            #if request has arrived, pop it off the queue
            req = queue.pop(0)
            #if request has remaining time greater than time quantum, process it and add it back to the queue
            if(req.remaining_time > time_quantum):
                req.remaining_time -= time_quantum
                #increment elapsed time by time quantum
                elapsed_time+= time_quantum
            
                queue.append(req)
            else:
                #if request has remaining time less than time quantum, process it and calculate turnaround and waiting time
                elapsed_time+=req.remaining_time
                req.remaining_time = 0
                turnaround[req.id] = elapsed_time - arrivals[req.id]
                req.wait_time = turnaround[req.id] - req.processing_time
        else:
            #if no requests have arrived, increment time to the first arrival
            elapsed_time = arrivals[queue[0].id]
          
    for req in requests:
        #print turnaround and waiting time for each request
        print(f"Request ID: {req.id}, Arrival Time: {arrivals[req.id]} Waiting Time: {req.wait_time}, Turnaround Time: {turnaround[req.id]}")
        #calculate total turnaround and waiting time
        total_wait_time += req.wait_time
        total_turnaround_time += turnaround[req.id]
        #reset request values
        req.wait_time = 0
        req.remaining_time = req.processing_time
    #print average turnaround and waiting time
    print(f"Average Waiting Time: {total_wait_time/len(requests)}")
    print(f"Average Turnaround Time: {total_turnaround_time/len(requests)}")



def first_come_first_serve(requests, arrivals):
    # This function will handle the first come first serve algorithm
    waiting_time_sum = 0
    turnaround_time_sum = 0
    elapsed_time = 0
    
    queue = []
    
    #add requests to queue
    for req in requests:
        queue.append(req)
    #sort queue by arrival time
    queue.sort(key=lambda x: arrivals[x.id])

    while(len(queue)>0):
        #check if request has arrived
        if (elapsed_time < arrivals[queue[0].id]):
            elapsed_time = arrivals[queue[0].id]
        else:
            #if request has arrived, pop it off the queue, process it and calculate waiting and turnaround time 
            request = queue.pop(0)
            waiting_time = elapsed_time - arrivals[request.id]
            elapsed_time += request.processing_time
            turnaround_time = waiting_time + request.processing_time

            #add waiting and turnaround time to total
            waiting_time_sum += waiting_time
            turnaround_time_sum += turnaround_time
        
            print(f"Request ID: {request.id}, Waiting Time: {waiting_time}, Turnaround Time: {turnaround_time}, Arrival Time: {arrivals[request.id]}")

    # print avg waiting time, avg turnaround time
    print(f"Average waiting time: {waiting_time_sum / len(requests)}\nAverage turnaround time:{turnaround_time_sum / len(requests)}")

    

def generate_random_requests(num_requests=20):
    import random
    
    # Generates a list of random client requests
    return [Request(i, random.randint(1, 10)) for i in range(num_requests)]

def main():
    import random
    requests = generate_random_requests()

    requests_tc1 = [Request(0, 3), Request(1, 2), Request(2, 4), Request(3, 5), Request(4, 1)]
    requests_tc2 = [Request(0, 4), Request(1, 6), Request(2, 8), Request(3, 2), Request(4, 4)]

    arrivals = {}

    #generate random arrival times
    for i in range(len(requests)):
        arrivals[i] = random.randint(0,10)

    for req in requests:
        print(f"Request ID: {req.id}, Processing Time: {req.processing_time}")
    #run the tests for multiple time quantum values
    for time_quantum in ([1,3,7]):

        print(f"Round Robin Time quantum: {time_quantum}")
        start_scheduling(requests, time_quantum,arrivals)
    print("First come first serve:")
    first_come_first_serve(requests, arrivals)

    # TODO: Calculate and display the average waiting time and average turnaround time

if __name__ == "__main__":
    main()

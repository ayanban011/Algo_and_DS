# Open the file in read mode
with open('info.txt', 'r') as file:
    # Read each line in the file
    count = 0
    n = 0
    jobs_weight = []
    jobs_length = []
    for line in file:
        # Print each line
        if(line.strip() != "" and count == 0):
            n = int(line.strip())
            count+=1
        else:
            l = line.strip()
            l1 = l.split(" ")
            jobs_weight.append(int(l1[0]))
            jobs_length.append(int(l1[1]))

    # Sort the jobs by the difference of weight and length
    # If the difference is the same, sort by weight
    # If the difference and weight are the same, sort by index
    jobs = []
    for i in range(n):
        jobs.append((jobs_weight[i], jobs_length[i], jobs_weight[i] - jobs_length[i], i))
    jobs = sorted(jobs, key=lambda x: (x[2], x[0], x[3]), reverse=True)

    # Calculate the weighted sum of completion times
    completion_time = 0
    weighted_sum = 0
    for job in jobs:
        completion_time += job[1]
        weighted_sum += job[0] * completion_time
    print(weighted_sum)    
            
            
        
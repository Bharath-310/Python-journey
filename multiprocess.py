from multiprocessing import Process
import time

def longsquare(num):
    time.sleep(1)  
    print(num**2)  # Prints the square of the number
    print('Finished computing')

# Creating processes targeting the `longsquare` function
processes= [Process(target=longsquare, args=(n,)) for n in range(10)]


# Start the processes
[p.start() for p in processes]

# Wait for process
[p.join() for p in processes]


# Output 
'''
0
Finished computing
1
Finished computing
4
Finished computing
9
Finished computing
16
Finished computing
25
Finished computing
36
Finished computing
49
Finished computing
64
Finished computing
81
Finished computing'''

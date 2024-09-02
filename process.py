from multiprocessing import Process
import time

def longsquare(num):
    time.sleep(1)  
    print(num**2)  # Prints the square of the number
    print('Finished computing')

# Create two processes targeting the `longsquare` function
p1 = Process(target=longsquare, args=(1,))
p2 = Process(target=longsquare, args=(2,))

# Start both processes
p1.start()
p2.start()

# Wait for both
p1.join()
p2.join()

# Output 
'''
1
Finished computing
4
Finished computing

[Process completed - press Enter]'''
import time # importing the Time module
import threading # importing thread module

def longsquare(num,result): 
    time.sleep(1)    # wait for a second 
    result[num]=num**2  # adding values to dictionary 
    
results={} # creating an empty dictionary 

t1=threading.Thread(target=longsquare,args=(1, results))  # creating a thread object
t2=threading.Thread(target=longsquare,args=(2,results))

t1.start()   # starting the thread 
t2.start()

t1.join()   # wait till thread completes 
t2.join()

print(results) # printing the result


#Output
'''
{1: 1, 2: 4}

[Process completed - press Enter]'''
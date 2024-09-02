import time # importing the Time module
import threading # importing thread module

def longsquare(num,results): 
    time.sleep(1)    # wait for a second 
    results[num]=num**2  # adding values to dictionary 
    
results={} # creating an empty dictionary 
threads=[threading.Thread(target=longsquare,args=(n, results)) for n in range (10)] # creating a thread object and looping the values 

[t.start() for t in threads]  # starting the thread and looping it
[t.join() for t in threads] # wait till thread completes and looping it
print(results) # printing the result
print('\n',(dict(sorted(results.items())))) #prining the sorted dictionary 


#Output
'''{0: 0, 1: 1, 3: 9, 6: 36, 2: 4, 4: 16
, 5: 25, 7: 49, 8: 64, 9: 81}

[Process completed - press Enter]'''
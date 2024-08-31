class CustomException(Exception): 
    pass 
def causeError(): 
    raise CustomException('You called the custom error function') 
causeError()    

'''Output:

 Traceback (most recent call last):
  File "/data/user/0/com.kvassyu.coding.py/files/default.py", line 5, in <module>
    causeError()
  File "/data/user/0/com.kvassyu.coding.py/files/default.py", line 4, in causeError
    raise CustomException('You called the custom error function')
    
__main__.CustomException: You called the custom error function'''
class HttpException(Exception): # extending to built in class Exception
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is: {self.message}') #parent class instance is initialised 
        
class NotFound(HttpException):
    statusCode = 404    
    message = 'Resource not found'
    
class ServerError(HttpException):
    statusCode = 500 # override statuscode and message 
    message = 'The server messed up!'
    
def raiseServerError():
    raise ServerError() # its like creating object instance for class ServerError
    
    
raiseServerError() #calling raiseServerError function 


#Output
'''Traceback (most recent call last):
  File "/data/user/0/com.kvassyu.coding.py/files/default.py", line 19, in <module>
    raiseServerError() #calling raiseServerError function
  File "/data/user/0/com.kvassyu.coding.py/files/default.py", line 16, in raiseServerError
    raise ServerError() # its like creating object instance for class ServerError
__main__.ServerError: Status code: 500 and message is: The server messed up!'''
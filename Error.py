#!/usr/bin/python3

def handlexception(func): 
    def wrapper(): 
        try: 
            func()
        except ZeroDivisionError: 
            print("there was zero division error") 
        except TypeError: 
            print("there was type error")    
        except Exception: 
            print("there was a error")      
    return wrapper     
      
    
    
    
    
    
    
@handlexception 
def causeError(): 
     return 1/0  
causeError()    
    
    
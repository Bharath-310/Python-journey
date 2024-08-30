varA=6 #global data
message='bla bla data' 


#function1
def function1(varA, varB): 
    print(locals()) 
    print(varA,message) #local data is checked first 
    
#fuction2
def function2(varC,varD): 
    try: 
        print(varB)
    except Exception: 
        print('there was an error')
        
    print(locals()) 
    print(varA, varC, message) #global data 


#Calling the function
function1(2,4) 
function2(5,7)
     
     
#output
'''{'varA': 2, 'varB': 4}
2 bla bla data
there was an error
{'varC': 5, 'varD': 7}
6 5 bla bla data'''

#output2 when no error in try block varD
''' {'varA': 2, 'varB': 4}
2 bla bla data
7
{'varC': 5, 'varD': 7}
6 5 bla bla data'''
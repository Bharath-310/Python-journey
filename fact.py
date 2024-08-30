for i in range(2,100): 
    for fac in range(2,int(i**0.5)+1): 
        if i%fac==0: 
            break 
            
    else: 
        print('the number {} is prime'.format(i)) 
              
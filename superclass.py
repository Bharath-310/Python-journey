class Dog: 
    
    _legs=4 
   
    def __init__(self): 
        self.name='Rower'
        self.type='Domestic'
   
    def speak(self):
        print(self.name +' has barked') 
        
    def who(self):
        print(self.name +' is a Dog')   #child class attribute is considered 
        
    def animal(self): 
        print('{} is a {} animal'.format(self.name,self.type))   
        
class Chic(Dog): 
    def __init__(self):
       super().__init__() #calls the parent class
       self.name='kyo' # overrides it names
    
    def who(self):
        print(self.name +' is a Duck')
    def speak(self): 
        print(self.name+' says flap flap flap')
    
mydog=Dog() 
mychic=Chic() 


print(mydog.name)
mydog.speak() 
mydog.who()
mydog.animal()
print('\n')

print(mychic.name)
mychic.speak()    #child class method is called 
mychic.who()      #child class attribute is considered 
mychic.animal()

print('\n{} and {} are friends'.format(mydog.name,mychic.name)) 

''' output
Rower
Rower has barked
Rower is a Dog
Rower is a Domestic animal


kyo
kyo says flap flap flap
kyo is a Duck
kyo is a Domestic animal

Rower and kyo are friends'''
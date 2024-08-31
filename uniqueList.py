mylist=list() 

class UniqueList(list): 
    def __init__(self):
        super().__init__() # making sure that parent class instance is called first 
        self.name='This is child class inherited by parent class List'
    def append(self,item):
        if item in self: 
            return
        super().append(item) 
        
        
objlist=UniqueList()
objlist.append(1)
objlist.append(1)
objlist.append(2) 

print(objlist)
print(objlist.name)        


'''Output
[1, 2]
This is child class inherited by parent class List
[Proce+ss completed - press Enter]'''
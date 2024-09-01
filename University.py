class University: 
    
    def __init__(self,name,message,course_list):
        self.name=name 
        self.message=message
        self.course_list=course_list
        
    def  displayInfo(self):
        print(f'university:{self.name}\nmessage:{self.message}')
        
    def courseOffered(self): 
        print('courses offered:{}\n'.format(','.join(self.course_list)))
            
        
class A_univ(University): 
    
    def __init__(self):
        name='Chennai'
        message=f'{name} institute is under AU'
        course_list=['Sciece','Technology','physics']
        super().__init__(name,message,course_list) 
        
    
class B_univ(University):
    
    def __init__(self):
        name='Coimbatore'
        message=f'{name} institute is under AU'
        course_list=['Computer','Mechanical','physics']
        super().__init__(name,message,course_list) 
               

a_university=A_univ() 
a_university.displayInfo()
a_university.courseOffered()

b_university=B_univ()   
b_university.displayInfo()
b_university.courseOffered()


#Output
'''university:Chennai
message:Chennai institute is under AU
courses offered:Sciece,Technology,physics

university:Coimbatore
message:Coimbatore institute is under AU
courses offered:Computer,Mechanical,physics


[Process completed - press Enter]'''
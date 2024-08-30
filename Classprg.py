class Wordset: 
   replace_func=['/',',','.','!'] 
   def __init__(self):
         self.words=set() 
         
   def addtext(self,text): 
        text=self.cleantext(text) 
        for word in text.split(): 
            self.words.add(word)
   
   @staticmethod     
   def cleantext(text): 
        for punc in Wordset.replace_func:
           text=text.replace(punc,'') 
        return text.lower()  
        
Wordset=Wordset() 
Wordset.addtext(' hi i/am Bharath and I am Adding my sentence down!!!') 
Wordset.addtext('this,, is the SenTence')    
print(Wordset.words) 

#output 
''' {'am', 'my', 'sentence', 'down', 'and', 'i', 'the', 'bharath', 'hi', 'this', 'adding', 'is', 'iam'}

[Process completed - press Enter]'''


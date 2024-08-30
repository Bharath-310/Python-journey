class Wordset: 
   
   def __init__(self):
         self.words=set() 
         
    def addtext(self,text): 
        text=self.cleantext(text) 
        for word in text.split(): 
            self.words.add(word)
        
    def cleantext(self,text): 
        text=text.replace('/','').replace(',','').replace('.','').replace('!','') 
        return text.lower()  
        
Wordset=Wordset() 
Wordset.addtext(' hi i/am Bharath and I am Adding my sentence down!!!') 
Wordset.addtext('this,, is the SenTence')    
print(Wordset.words) 

#output 
''' {'am', 'my', 'sentence', 'down', 'and', 'i', 'the', 'bharath', 'hi', 'this', 'adding', 'is', 'iam'}

[Process completed - press Enter]'''
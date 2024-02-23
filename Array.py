# my code 
class Array(object):

    def __init__(self, initialSize):  #class constructor
        self.__a = [None] * initialSize   #the array out in memory
        self.__nItems= 0  #number of items in the array

    #add the following three functions:
    def __len__(self):
        return self.__nItems

    #getMethod
    def get(self,n):
        if 0 <= n < self.__nItems:
            return self.__a[n]

    #setMethod
    def set(self,n,value):
        if 0<= n < self.__nItems:
            self.__a[n]= value
            
    def swap(self, i, k):
        if (0 <= i and i< self.__nItems and 
            0 <= k and k< self.__nItems):
            self.__a[i], self.__a[k] =  self.__a[k], self.__a[i]

    #update insert with a raise exception
    def insert(self, item): #basic insert into the array struct
        if self.__nItems >= len(self.__a):
            raise Exception ("Overflow")
        self.__a[self.__nItems] =item   #put the item at the end of the array
        self.__nItems +=1 #increment where the end is 

    def find(self, item):
        for i in range(self.__nItems):
            if(self.__a[i]==item):
                return i     #return index of item
        return -1
    
    def search(self, item):
        return self.get(self.find(item))

    def delete(self,item):
        for i in range(self.__nItems):
            if self.__a[i] ==item:
                self.nItems-= 1
                for k in range(i, self.__nItems):
                    self.__a[k] = self.__a[k +1]
            
                return True
    
        return False #item not in the array 
        
    def traverse(self,function = print):  #apply some function to each item in the array
        for i in range(self.__nItems):  #by defult this is print statemnet
            function(self.__a[i]) 
            
    def __str__(self):
        value = "["
        for i in range (self.__nItems):
            if len(value)> 1:
                value += ", "
            value += str(self.__a[i])
        value += "]"
        return value
    
    #adding sorting methods to this class:
    def bubbleSort(self):
        for last in range(self.__nItems-1,0, -1):
            for i in range(last):
                if self.__a[i] > self.__a[i+1]:
                    self.swap(i, i+1)
                    
    def insertionSort(self):
        for o in range(1,self.__nItems):
            currentValue = self.__a[o]
            i = o 
            while i > 0 and currentValue < self.__a[i-1]:
                self.__a[i]= self.__a[i-1]
                i -=1
            self.__a[i]= currentValue
                
    def selectionSort(self):
        for o in range(self.__nItems-1):
            min= o
            for i in range(o + 1, self.__nItems):
                if self.__a[i] < self.__a[min]:
                    min= i
            self.swap(o, min)
               
            
                
           
                
                
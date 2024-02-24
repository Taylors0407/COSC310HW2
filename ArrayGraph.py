#Taylor Serrano homework 2 
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
            return self.__a[n] #gets value at n

    #setMethod
    def set(self,n,value):
        if 0<= n < self.__nItems:
            self.__a[n]= value #finds specific index and changes value 
            
    def swap(self, i, k):
        if (0 <= i and i< self.__nItems and 
            0 <= k and k< self.__nItems):
            self.__a[i], self.__a[k] =  self.__a[k], self.__a[i] #can look at next value or previous value (depends on index)and swap

    #update insert with a raise exception
    def insert(self, item): #basic insert into the array struct
        if self.__nItems >= len(self.__a):
            raise Exception ("Overflow")
        self.__a[self.__nItems] =item   #put the item at the end of the array
        self.__nItems +=1 #increment where the end is 

    def find(self, item): 
        for i in range(self.__nItems): #the length of self
            if(self.__a[i]==item): #when index equals what is trying to be found
                return i     #return index of item
        return -1  #returns negative int if item not found
    
    def search(self, item):
        return self.get(self.find(item)) #will use the find to locate what item is at an index

    def delete(self,item):
        for i in range(self.__nItems):#looking at array
            if self.__a[i] ==item: #finding item in array
                self.nItems-= 1 #deleting 
                for k in range(i, self.__nItems):
                    self.__a[k] = self.__a[k +1] #replacing space with next item 
            
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
            currentValue = self.__a[o]  #Get temp value to compare in part sorted array
            i = o 
            while i > 0 and currentValue < self.__a[i-1]: #finding where it goes
                self.__a[i]= self.__a[i-1]
                i -=1
            self.__a[i]= currentValue #is now equal to that value
                
    def selectionSort(self):
        for o in range(self.__nItems-1):
            min= o #left most thjng is minimum
            for i in range(o + 1, self.__nItems):
                if self.__a[i] < self.__a[min]:
                    min= i
            self.swap(o, min) #single swap
    import random
    import timeit

    low= 10
    high= 20

    def MakeArray(size = random.randint(low,high), maxVal = 1000, seed = 42):
    random.seed(seed)
    A = Array(size)
    for i in range(size):
        A.insert(random.randrange(maxVal))
    return A

    A= MakeArray()
    print(A)
    
    
    timeList1= []
    timeList2= []
    timeList3= []

    time1 = timeit.timeit('MakeArray().bubbleSort()', number = 100, globals = globals())
    print("Timing1: ",time1)
    timeList1.append(time1)

    time2 = timeit.timeit('MakeArray().insertionSort()', number = 100, globals = globals())
    print("Timing2: ",time2)
    timeList2.append(time2)

    time3 = timeit.timeit('MakeArray().selectionSort()', number = 100, globals = globals())
    print("Timing3: ",time3)
    timeList3.append(time3)

    print(timeList1, timeList2, timeList3)
    
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import figure
    import numpy as np


    x1 = timeList1
    y1 = timeList1

    x2= timeList2
    y2= timeList2

    x3= timeList3
    y3= timeList3



    plt.scatter(x1, y1, c='red')
    plt.scatter(x2, y1, c='green')
    plt.scatter(x3, y1, c='blue')


    #labeling the graph
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Random plots")
    plt.show()
#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import random
/*
arr = random.randint(500,size=(50))
maxim = arr[0]
minim = arr[0]
c1=0
for num in arr:
    if(num >maxim):
        c1=c1+1
        maxim = num
    elif(num < minim):
        c1=c1+1
        minim = num
    c1+=1    
print("max =", maxim, "min =", minim, "comparisons = ", c1)
*/

def driver(low, high):
    global c2
    if(low == high):
        c2=c2+1
        ma = mi = arr[high]                
        return [ma,mi]

    if(high == low+1):
        c2=c2+1
        if(arr[high]>arr[low]):
            ma = arr[high]
            mi = arr[low]
        else:
            ma = arr[low]
            mi = arr[high]
        return [ma,mi]
    mid = int((low+high)/2)
    larr = driver(low, mid)
    rarr = driver(mid+1, high)
    if(larr[0]>rarr[0]):
        ma = larr[0]
    else:
        ma = rarr[0]
    if(larr[1]<rarr[1]):
        mi = larr[1]
    else:
        mi = rarr[1]

    return [ma,mi]


c2=0
#arr = random.randint(500,size=(50))
arr= [0,1,2,1,2,1,2,0,1,2,2,1,0,1,2,1]
x = driver(0,10)
print("max = ", x[0], "\nmin =", x[1],"\ncomparisons = ", c2)


# In[4]:


def sort012():   
    for j in range(1,len(arr)):
            while( j>0 and (arr[j] <arr[j-1] )):
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                j=j-1
    return arr  


#arr = random.randint(3, size= 10)
print(arr)
x = sort012()
print(x)





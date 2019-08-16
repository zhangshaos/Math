#@time:     2019.8.14
#@Author:   CZ
#@Name:     Mergesort Algorithm


import numpy as np



def Mergesort(array,start,end):
    if(end-start>0):
        m = (start+end)//2
        Mergesort(array,start,m)
        Mergesort(array,m+1,end)
        Merge(array,start,m,end)
    #else: donothing...




def Merge(array,start,m,end): #@param:m is the array's middle element,which devide the whole array into two piece:array[:m+1],array[m+1:len(array)]
    l = start
    r = m+1
    sorted = []
    while(l<=m and r<=end):
        if(array[l]<array[r]):
            sorted.append(array[l])
            l+=1
        else:
            sorted.append(array[r])
            r+=1
    while(l<=m):
        sorted.append(array[l])
        l+=1
    while(r<=end):
        sorted.append(array[r])
        r+=1
    assert(len(sorted)==end-start+1)
    print(sorted)
    i = 0
    j = start
    while(i<len(sorted)):
        array[j]=sorted[i]
        j+=1
        i+=1
    assert(j==end+1)
    print(array)


#Main():
unsorded = []
i = 0
while(i<100):
    unsorded.append(np.random.randint(-50,50))
    i+=1
print(unsorded)
Mergesort(unsorded,0,i-1)
print(unsorded)

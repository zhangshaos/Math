#@Time:19.8.16
#@Author:CZ


import numpy as np



def Quicksort(A,start,end):
    if(end - start > 0):
        # m means the pivot of A
        m = Partition(A,start,end,(start+end)//2)
        print(A[start:m+1])
        print(A[m+1:end+1])
        Quicksort(A,start,m-1)
        #m is middle,so do nothing
        Quicksort(A,m+1,end)



#divide the array into three parts:
# (less the element whose index is m, m, bigger the element whose index is m)
def Partition(A,start,end,m):
    assert(m<=end and m>=start)
    # list_swap(A,start,m)
    # less = start #the last element less than A[start]
    # tail = end
    # i = start
    # while(i<=tail):
    #     if(A[i]<=A[start]):
    #         less = i
    #         i+=1
    #     else:
    #         list_swap(A,i,tail)
    #         tail-=1
    # list_swap(A,start,less)
    # return less
    list_swap(A,m,end)
    less = start
    i = start
    while(i<end):
        if(A[i]<A[end]):
            list_swap(A,i,less)
            less += 1
        i+=1
    list_swap(A,end,less)
    return less



def list_swap(A,a,b):
    if(a != b):
        tmp = A[a]
        A[a] = A[b]
        A[b] = tmp


def Main():
    unordered = []
    for i in range(0,100):
        unordered.append(np.random.randint(-50,50))
    print(unordered)
    Quicksort(unordered,0,len(unordered)-1)
    # list_swap(unordered,0,1)
    print(unordered)
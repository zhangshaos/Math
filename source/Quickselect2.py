



import Quicksort as qs
import time as T

def Quickselect(A,ordinal):
    assert (ordinal<=len(A))
    if(len(A)==1):
        return A[0]
    else:
        pivot = ordinal-1
        loca = Parttion(A,pivot)
        next_search_dir = Searchdir(A,loca,ordinal)
        if(0==next_search_dir):
            return A[loca]
        elif(1==next_search_dir):
            return Quickselect(A[loca+1:],ordinal-Getordinal(A,loca))
        else:
            return Quickselect(A[:loca],ordinal)




def Parttion(A,p):
    end = len(A)-1
    assert (p<=end)
    qs.list_swap(A,p,end)
    less = 0
    i = 0
    while(i<end):
        if(A[i]<A[end]):
            qs.list_swap(A,less,i)
            less+=1
        i+=1
    qs.list_swap(A,less,end)
    return less


def Searchdir(A,p,ordinal):
    i = 0
    unrepeated = set()
    while(i<=p):
        unrepeated.add(A[i])
        i+=1
    l = len(unrepeated)
    if(ordinal>l):
        return 1
    elif(ordinal<l):
        return -1
    else:
        return 0

def Getordinal(A,p):
    i = 0
    unrepeated = set()
    while(i<=p):
        unrepeated.add(A[i])
        i+=1
    return len(unrepeated)


def Main():
    unsored = []
    i = 100000
    while(i>=0):
        unsored.append(i)
        i-=1
    # unsored = [0,0,0,0,0]
    print(unsored)
    print("Quickselect2: Input the ordinal:")
    ordinal = input()
    origt = T.process_time()
    ret = Quickselect(unsored,int(ordinal))
    endt = T.process_time()
    print(unsored)
    print("The",ordinal,"th ele is:",ret)
    print("Algorithm time:",endt-origt)

Main()
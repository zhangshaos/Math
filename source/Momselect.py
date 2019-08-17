

import Quicksort as qsort
import Quickselect2 as Qs2
import time as T
import numpy as np



def Momselect(A,ordinal):
    assert (ordinal<=len(A))
    if(len(A)<25):
        #use other algorithm
        return Qs2.Quickselect(A,ordinal)
    else:
        blocks = len(A)//5  # we throw the odd
        middles = []
        i = 1
        while(i<=blocks):
            middles.append(MiddleOfFive(A[5*i-5:5*i]))
            i+=1
        mom = Momselect(middles,blocks//2)

        p = Parttion(A,mom)
        next_dir = Qs2.Searchdir(A,p,ordinal)
        if(next_dir==0):
            return mom
        elif(next_dir==1):
            return Momselect(A[p+1:],ordinal-Qs2.Getordinal(A,p))
        else:
            return Momselect(A[:p],ordinal)





def MiddleOfFive(Five):
    return Qs2.Quickselect(Five,3)


# divide A by @param:value  into three part(small,equal,big)
def Parttion(A,value):
    i = 0
    less = 0
    while(i<len(A)):
        if(A[i]<value):
            qsort.list_swap(A,less,i)
            less+=1
        i+=1
    assert (less<len(A))
    return less


def Main():
    unsored = []
    i = 100000
    while(i>=0):
        unsored.append(i)
        i-=1
    # unsored = [0,0,0,0,0]
    print(unsored)
    print("Momselect: Input the ordinal:")
    ordinal = input()
    origt = T.process_time()
    ret = Momselect(unsored,int(ordinal))
    endt = T.process_time()
    print(unsored)
    print("The",ordinal,"th ele is:",ret)
    print("Algorithm time:",endt-origt)

Main()
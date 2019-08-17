# @Time: 19,8,17
# @Author: CZ


import  numpy as np
import Quicksort as qs


def Quickselect(A,head,tail,k):
    assert (head <= tail)
    r = Parttion(A,head,tail,k)
    if(k<r):
        return Quickselect(A,head,r-1,k)
    elif(k>r):
        return Quickselect(A,r+1,tail,k)
    else:
        return A[r]








def Parttion(A,head,tail,m):
    assert (head <= tail)
    qs.list_swap(A,m,tail)
    less = head
    i = head
    while(i<tail):
        if(A[i]<A[tail]):
            qs.list_swap(A,less,i)
            less+=1
        i+=1
    qs.list_swap(A,less,tail)
    return less




# unordered = [10,9,8,7,6,5,4,3,2,1]
unordered = []
for i in range(0,10):
    unordered.append(np.random.randint(-5,5))
print(unordered)
_3th_less_ele = Quickselect(unordered,0,len(unordered)-1,3-1)
print(_3th_less_ele)
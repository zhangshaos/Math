# Math
some joy......



[1.古典概率题](#一个古典概率问题)

[2.寻找中位数](#无序数列中寻找中位数)(*find the median of an array*)

[3.N queens](#N queens)



---

##  一个古典概率问题

[Q & A](./19.8.1.0.md)

## 无序数列中寻找中位数

*fine the median of an unsored array in linear time.*

`核心: 中位数一个序列中中间大小的数, 也就是说, 有len/2个数小于该中位数(这len/2个数字的顺序无关),由此可以想到Parttion算法-用pivot代表那个中位数`



## N queens
1. [**'Backtracking'** solution](./source/PlaceQueens.py)





---

## Algorithm

[1.Mergesort](#Mergesort)

[2.Quicksort](#Quicksort)

[3.Qucikselect](#Quicksort)

* [Momselect](#Momselect)



---

### Mergesort

The core is `merge`,[source here](./source/Mergesort.py)

This Algorithm alse adapt to list and tree.

### Quicksort

The core is `diveide one to three`,[source here](./source/Quicksort.py)

This Algorithm also adapt to list, but not tree(I can not Parttion the tree now.)



### Quickselect
The core is `Parttion(the pivot is Xth smallest element)`,[source here](./source/Quickselect1.py)

==@bugs==: There is a bug where the pivot is not the Xth smallest element if there are the same ele in array.

==@example==: [-4,-4,-4,0,1,2,3,4], Quickselect(Array,4-1)=0(not 2) 

[Fixed version](./source/Quickselect2.py)

> Actually,  In "Fixed version", there are also bugs... If your iniput is [0,0,0,0] and find 3th smallest ele, this algorithm return 0(actually, it should return nothing)

==@Analysis==:

```python
def Quickselect(A,ordinal):
    assert (ordinal<=len(A))
    if(len(A)==1):
        return A[0]
    else:
        pivot = ordinal
        loca = Parttion(A,pivot)
        next_search_dir = Searchdir(A,loca,ordinal)
        if(0==next_search_dir):
            return A[loca]
        elif(1==next_search_dir):
            return Quickselect(A[loca+1:],ordinal-Getordinal(A,loca))
        else:
            return Quickselect(A[:loca],ordinal)
```

**T(N) = O(N) + MAX{ T(loca) , T(N - loca) }**

If we make `loca` = `N - loca`(->`loca = N/2`), the T(N) will decrease quickly.

So how can we make the `loca` because `N/2`,  and the key is that make the element `pivot` points to be the midian of A.

So let's get the midian's index `pivot`as far as possible.

![tips](./source/Mom.jpg)

### Momselect

developed `Quickselect`,[source here](./source/Momselect.py)
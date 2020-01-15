> Here a copy of answer when I read 《数据结构与算法分析 Mark Allen Weiss著》is.

### Chapter 3(List)

**3.34**

* Given there a unknown-length list including a circle, how to determine weather the list contains a circle?
* time O(N)
* space O(1)

example: 

```c++
// a -> b -> c -> d -> b
```

solution:

> Create two iterators that both point to the start of list and run at different speed.
>
> if there is a circle in the list, the two iterators will meet again somewhere!
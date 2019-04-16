#策略：搜索整个列表，找到最小项的位置。如果该位置不是列表的第1个位置，算法就会交换在这两个位置的项，然后，算法回到第2个位置并且重复这个过程，如果必要的话，将最小项和第2个位置的项交换。当算法到达整个过程的最后一个位置，列表就是排序好的了
#小->大
def selectionsort(lyst):
    i = 0
    while i<len(lyst)-1:
        minindex=i
        j=i+1
        while j<len(lyst):
            if lyst[j]<lyst[minindex]:
                minindex = j
            j += 1
        if minindex != i:
            lyst[minindex],lyst[i] = lyst[i],lyst[minindex]
        i += 1
    return lyst

#该函数包含了一个嵌套循环。对于大小为n的列表，外围的循环执行n-1次。在第1次通过外围的循环的时候，内部的循环回执行n-1次。在第2次循环的时候，内部的循环回执行n-2次。在外围循环最后一次执行的时候，内部循环执行一次。
#对于一个大小为n的列表，总的比较次数为：(n-1)+(n-2)+(n-3)+...+1 = n(n-1)/2 = 1/2*n^2-1/2*n
#各种情况下复杂度O(n^2)
lista =[6,4,3,34,5,67,7,3,4]
print(selectionsort(lista))
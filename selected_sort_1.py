def my_sort(alist):
    for i in range(len(alist)):
        minindex=i
        for j in range(i+1,len(alist)):
            if alist[i]>alist[j] :
                minindex =j
        alist[i],alist[minindex] = alist[minindex],alist[i]
a=[2,3,1,2,4,9,9,9]
my_sort(a)
print(a)


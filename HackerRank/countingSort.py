def countingSort(arr):
    le = len(arr)
    a= [0]*le
    # for i in range(le):
    #     a.append(0)
    # arr.sort()
    for i in range(le):
        a[arr[i]] = a[arr[i]]+1
    return a
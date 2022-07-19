#=============================== Comparison Sorting ===========================================
# Example
# arr = [1,1,3,2,1]

# All of the values are in the range[0....3] , 
# so create an array of zeros, result = [0,0,0,0].
# The results of each iteration follow

# i	arr[i]	result
# 0	1	[0, 1, 0, 0]
# 1	1	[0, 2, 0, 0]
# 2	3	[0, 2, 0, 1]
# 3	2	[0, 2, 1, 1]
# 4	1	[0, 3, 1, 1]
# ======================== HackerRank ============================================

def countingSort(arr):
    le = len(arr)
    m = int(max(arr))
    a= [0]*(m+1)
    for i in range(le):
        a[int(arr[i])] = a[int(arr[i])]+1
    print(a) 

f = open('countingSort.text','r')
a = f.readline()
c= f.readline()
b = list(c.split(" "))
countingSort(b)

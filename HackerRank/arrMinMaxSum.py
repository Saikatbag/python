# =======================minimum and maximum Sum of Arr====================
# Given five positive integers, find the minimum and maximum values         
# that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single 
# line of two space-separated long integers.
# Example
# arr = [1, 3, 5, 7, 9]
# The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum 
# is 3 + 5 + 7 + 9 = 24 . The function prints 16 , 25
# ============================== HackerRank ================================

def miniMaxSum(arr):
    arr.sort()
    max = 0
    min = 0 
    for i in range(1,len(arr)):
        max = max + int(arr[i])
    for i in range(0,len(arr)-1):
        min = min + int(arr[i])
        
    print( min, max)

arr = [1, 3, 5, 7, 9]
miniMaxSum(arr)
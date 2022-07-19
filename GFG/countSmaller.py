# ======================================= Count Smaller elements ===================================
# Given an array Arr of size N containing positive integers. Count number of smaller elements on 
# right side of each array.

# Example 1:

# Input:
# N = 7
# Arr[] = {12, 1, 2, 3, 0, 11, 4}
# Output: 6 1 1 1 0 1 0
# Explanation: There are 6 elements right
# after 12. There are 1 element right after
# 1. And so on
# ================================ GFG ======================================================
def constructLowerArray(arr, n):
	for i in range(n):
		val = arr[i]
		count = 0
		for j in range(i+1,n):
			if(val>arr[j]):
				count = count + 1
				arr[i] = count
	print(arr)
arr = [12, 1, 2, 3, 0, 11, 4]
constructLowerArray(arr,7)
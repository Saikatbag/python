# -------------------------------Majority Element-------------------------------------
# ===================================================================================
# Given an array A of N elements. Find the majority element in the array. 
# A majority element in an array A of size N is
# an element that appears more than N/2 times in the array.
# Example
# Input:
# N = 5 
# A[] = {3,1,3,3,2} 
# Output:
# 3
# Explanation:
# Since, 3 is present more
# than N/2 times, so it is 
# the majority element
# =================================== 1st Approch =================================================
# N = 5 
# A = [3,1,3,3,3,2]
# c= N/2
# d = 0
# k= 0
# for i in range(N):
#     if (A.count(A[i])>k):
#         k = A.count(A[i])
#         d = A[i]
# if (k>N/2):
#     print(d)
# else:
#     print(-1)
# ====================Your program took more time than expected=====================================
# ====================Please optimize your code and submit again.===================================
# ==============================20/121---Test case pass --gfg code====================================



# ===================================== 2nd Approch ================================================
   
N = 2 
A = [6,16]
c= N/2
d = 0
k= 0
s = set(A)
for i in s:
    if (A.count(i)>k):
        k = A.count(i)
        d = i
if (k>N/2):
    print(d)
else:
    print(-1)

# ===============================Your program took more time than expected=====================
# ===============================Please optimize your code and submit again.===================
# ==========================================28/121---Test cate pass ---gfg code ====================
# ==================================================================================================

# https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1?page=1&category[]=Queue&sortBy=submissions
# ========================================Implement Queue using array====================================================
# Implement a Queue using an Array. Queries in the Queue are of the following type:
# (i) 1 x   (a query of this type means  pushing 'x' into the queue)
# (ii) 2     (a query of this type means to pop element from queue and print the poped element)

# Example 1:
# Input:
# Q = 5
# Queries = 1 2 1 3 2 1 4 2
# Output: 2 3
# Explanation:
# In the first test case for query 
# 1 2 the queue will be {2}
# 1 3 the queue will be {2 3}
# 2   poped element will be 2 the 
#     queue will be {3}
# 1 4 the queue will be {3 4}
# 2   poped element will be 3 
# ==========================================  GFG  ==========================================================
class MyQueue:
    def __init__(self):
        self.queue = []
    def push(self, x):    
        self.queue.append(x)
    def pop(self): 
        if self.queue == []:
            return -1
        else:
            t = self.queue[0]
            self.queue.pop(0)
            return t
    


if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   


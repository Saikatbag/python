# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#  determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# ======================================================================
class Solution:
    def match(self, a,b):
        if (a == '(' and b == ')'):
            return 1
        elif (a == '{' and b == '}'):
            return 1
        elif (a == '[' and b == ']'):
            return 1
        else:
            return 0
    def isValid(self, s: str) -> bool:
        stack = []
        le = len(s)
        if le ==1:
            return 0
        for i in range(le):
            if s[i] == "("or s[i] == "{" or s[i] == "[":
                stack.append(s[i])  
            elif (len(stack) != 0):
                if(self.match(stack[-1],s[i]) == 0 ):
                    break
            elif( len(stack)==0 and s[i]):
                return 0
            else:
                stack.pop()
        
        if(len(stack) == 0):
            return 1
        else:
            return 0
        
#https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n):
        a,b=0,1
        if n<=2:
            return n
        else:    
            for i in range(n):
                a,b=b,a+b
            return b
            

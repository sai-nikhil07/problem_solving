# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        
        s=set()
        while n!=1 and n not in s:
            s.add(n)

            dig=[int(dig) for dig in str(n)]
            n = sum(x**2 for x in dig)

        return n==1

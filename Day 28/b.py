# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # a=sorted(t) #t=aea   s= ae
        # return a[-1]
        s=sorted(s)
        t=sorted(t)

        for i in range(len(s)):
            if s[i]!=t[i]:
                return t[i]
        return t[-1]

# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
       # a=s.reverse()
        # s.reverse()
        #optimised or interview friendly 
        l,r=0,len(s)-1

        while l<r:

            s[l],s[r]=s[r],s[l]

            l+=1
            r-=1

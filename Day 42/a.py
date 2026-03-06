#https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        a=0
        for i in range(len(s)):
            if s[i]=="1" and (i==0 or s[i-1]=="0"):
                a+=1
        return a<=1
#or
        if "01" in s:
            return False
        else:
            return True

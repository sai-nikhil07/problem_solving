# https://leetcode.com/problems/hamming-distance/description/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        t=x^y
        c=0
        while t:
            c+=t&1
            t>>=1
        return c

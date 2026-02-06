# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:

        a=str(bin(n))

        return (a.count("1"))

        #optimised way

        nt = 0
        while n:
            n = n & (n - 1)
            nt += 1
        return nt
      

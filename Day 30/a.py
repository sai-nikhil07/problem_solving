#https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        
        bina=bin(n)[2:]
        bina=bina.zfill(32)
        rev=bina[::-1]
        return int(rev,2)

        #optimized 

        res = 0
    
        for _ in range(32):
            res<<= 1        # make space on right
            res|= (n & 1)   # add last bit of n
            n >>= 1             # move to next bit
        
        return res

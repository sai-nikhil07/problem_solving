# https://leetcode.com/problems/complement-of-base-10-integer/
# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        
        num= str(bin(num)[2:])
        fl=""
        for i in num:
            fl+=str(int(i)^1)
        return int(fl,2)

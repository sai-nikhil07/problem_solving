# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        res=0
        
        if x<0:
            x=str(x)[1:]
            x= "-"+str(x)[::-1]
            res=int(x)
        else :
            x=str(x)[::-1]
            res=int(x)

        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        return res

        # cleaner version

        # sign = -1 if x < 0 else 1
        # reversed_str = str(abs(x))[::-1]
        # res = sign * int(reversed_str)

        # if res < -2**31 or res > 2**31 - 1:
        #     return 0
        
        # return res

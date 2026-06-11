# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        s=0
        p=1

        while n:

            d= n%10

            p = p*d
            s = s+d 
            n//=10

        return p-s

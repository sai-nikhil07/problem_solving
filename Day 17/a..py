# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >=10:
    
            b= [int(d) for d in str(num)]
                
            num=sum(b)
        return num

            # optimised

        if num==0:
            return 0
        else:
            return (1 + (num - 1) % 9)
          

#https://leetcode.com/problems/base-7/
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0 : return "0"
        rem=[]
        if num>0:
            while num > 0:
                
                rem.append(num%7)
                num=int(num/7)

            return "".join(map(str,rem[::-1]))
            
        if num<0:
            
            while abs(num) > 0:
                rem.append(abs(num)%7)
                num=int(abs(num)/7)

            return "-"+("".join(map(str,rem[::-1])))

        ## optimised
        if num == 0:
            return "0"
        
        sign = ""
        if num < 0:
            sign = "-"
            num = abs(num)
        
        rem = []
        
        while num > 0:
            rem.append(str(num % 7))
            num = num // 7
        
        return sign + "".join(rem[::-1])

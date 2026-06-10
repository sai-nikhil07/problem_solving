# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r=[]
        for i in range(left , right+1):

            f= 0
            t=i
            while t:
                d = t%10 

                if d == 0 or i%d !=0:
                    f=1
                    break
                t//=10
            
            if f==0:
                r.append(i)
        
        return r

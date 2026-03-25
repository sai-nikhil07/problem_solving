https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:

        li=list(range(n+1))

        res=[]
        for i in li:
            res.append(bin(i)[2:].count("1"))

        return res  

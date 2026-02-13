# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        co=0
        mx=0

        for n in nums :
            if n==1:
                co+=1
                mx=max(co,mx)
            else :
                co=0
        
        return mx

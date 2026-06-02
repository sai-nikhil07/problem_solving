# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res= [ ]
        t= 0
        for i in nums:

            t+=i
            res.append(t)
            
        return res

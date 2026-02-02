#https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # tried
        for i in nums:
            if nums.count(i)!=2:
                return i
        
        # optimized (bitwise)

         re=0
        for i in nums:
            re^=i
        return re

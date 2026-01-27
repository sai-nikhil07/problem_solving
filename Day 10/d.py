# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * (len(nums))
        a= 1

        for i in range(len(nums)):
            res[i] = a
            a*= nums[i]

        b = 1

        for i in range(len(nums) -1, -1, -1):
            res[i] *= b
            b *= nums[i]
        return res

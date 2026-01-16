#   https://leetcode.com/problems/search-insert-position/?envType=problem-list-v2&envId=binary-search&roomId=IzoLkM

class Solution:
    def searchInsert(self, nums,target):

        for i in nums: 
            if i == target:  
                return nums.index(i)
            for i in range (len(nums)): 
                if nums[i]>=target: 
                    return index(i)
        return len(nums) 
        
        
    #  or
        
    def searchInsert(self, nums,target):
        if target in nums:
            return nums.index(target) 
        
        for i in range(len(nums)): 
           if nums[i] > target: 
                return i 
        return len(nums) 
        
        
        

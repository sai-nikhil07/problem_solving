#https://leetcode.com/problems/remove-element/description/
class Solution:
    def removeElement(self, nums, val) :
        #k=0 # temp
        
        while val in nums:  #v=2
            nums.remove(val)  # 3   
        return len(nums) # to return length of nums
        
            # or
            
# class Solution:
#     def removeElement(self, nums, val):
#         k = 0  #temp
#         for i in nums:
#             if i != val: # check the values with val if true goes to the next condition else return k if false incriment K
#                 nums[k] = i
#                 k += 1
#         return k

# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # l=[]
        # r=[]

        # for i in range (len(nums)) :
            
        #     if nums[i] == 0:
        #         l.append(nums[i])
        #     elif nums[i]!=0:
        #         r.append(nums[i])
                
        # nums[:] = r+l

        # or

        pos = 0

        for n in nums: # 0 1 0 3 12
            if n != 0: 
                nums[pos] = n # 1 3 12
                pos += 1 # 1 2 3

        for i in range(pos, len(nums)):
            nums[i] = 0 

    #nums = [0,1,0,3,12]
            # 1,3,12

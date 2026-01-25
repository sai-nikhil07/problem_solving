#https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()

        l=0
        r=k-1
        #res=[]

        res=float("inf")

        while r < len(nums):

            res= min(res, nums[r]-nums[l])
            #res.append(nums[r]-nums[l])
            l+=1
            r+=1
        return res

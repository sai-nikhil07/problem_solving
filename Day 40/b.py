#https://leetcode.com/problems/maximum-gap/ 

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
# its not a linerlinear time solution (O(n)) its n(log n) cz of sorting

        if len(nums)<2:
            return 0

        nums.sort()

        t=[]

        for i in range(len(nums)-1):
                
            t.append(nums[i+1]-nums[i])

        return max(t)

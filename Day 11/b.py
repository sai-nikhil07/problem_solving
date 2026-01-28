#https://leetcode.com/problems/majority-element/post-solution

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count={}

        for i in nums:
            count[i]=count.get(i,0)+1
        
        return max(count, key=count.get)

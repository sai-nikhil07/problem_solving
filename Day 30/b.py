# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # i know its not a optimal solution i just checked if this works or not

        res = sorted(nums1 + nums2)
        n = len(res)
        
        if n % 2 == 1:
            return res[n//2]
        else:
            return (res[n//2 - 1] + res[n//2]) / 2

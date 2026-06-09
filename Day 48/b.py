# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # nums.sort()
        l=[x for x in nums if x < pivot]
        e=[x for x in nums if x == pivot]
        g = [x for x in nums if x> pivot]

        return l + e + g

        # for i in nums:
        #     if i <pivot:
        #         l.append(i)
        #     elif i>pivot:
        #         l1.append(i)
        #     elif i == pivot:
        #         l2.append(i)
        
        # return l + l2 + l1

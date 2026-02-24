# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        
        self.pre=[]
        to=0

        for n in nums:
            to+=n
            self.pre.append(to)

    def sumRange(self, left: int, right: int) -> int:
        
        if left == 0:
            return self.pre[right]
        
        return self.pre[right]-self.pre[left-1]
       

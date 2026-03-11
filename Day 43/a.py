# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        l={}

        for i in nums:
            l[i]= l.get(i,0)+1
        
        s= dict(sorted(l.items(),key= lambda i : i[1]))

        r=list(s.keys())[-k:]
        return r


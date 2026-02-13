# https://leetcode.com/problems/shuffle-the-array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        a1 = nums[:n]
        a2= nums[n:]
        res=[]

        for i in range(len(a1)):
            
            res.append(a1[i])
            res.append(a2[i])

        return res

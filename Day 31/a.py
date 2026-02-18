# https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        tp= set(candyType)
        maxx= len(candyType)//2

        if len(tp) < maxx: return (len(tp))
        else: return maxx
        # or
        # return min(len(tp), maxx)
        # or 
        # return min(len(set(candyType)), len(candyType)//2)

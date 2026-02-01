# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0      # total flowers we can place
        zeros = 1      # virtual zero at start
        
        for x in flowerbed:
            if x == 0:
                zeros += 1
            else:
                count += (zeros - 1) // 2
                zeros = 0
        
        zeros += 1     # virtual zero at end
        count += (zeros - 1) // 2
        
        return count >= n

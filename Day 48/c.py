# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # c=0
        # for j in jewels:
        #     c+=stones.count(j)
        # return c

        return sum(stones.count(j) for j in jewels)

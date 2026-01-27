# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        d = int("".join(str(i) for i in digits)) + 1
        result = [int(x) for x in str(d)]

        return result


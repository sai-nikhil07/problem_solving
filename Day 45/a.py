# https://leetcode.com/problems/super-pow/
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        m= 1337
        s= 1
        for digit in b:
            s= pow(s, 10,m) * pow(a, digit,m) %m
        return s

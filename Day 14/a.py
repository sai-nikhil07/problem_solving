#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        se= set()
        le= 0
        ma =0

        for ri in range(len(s)):
            
            while s[ri] in se:
                se.remove(s[le])
                le += 1

            se.add (s[ri])
            ma =max(ma, ri - le + 1)

        return ma

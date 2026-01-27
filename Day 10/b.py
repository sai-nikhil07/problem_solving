# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d=s.split()

        return len(d[-1])

# algorithm way optimised
"""
        class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        
        # skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # count last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length


"""

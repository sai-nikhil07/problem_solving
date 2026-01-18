# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        fi=""

        r=0
        l=0
      
        while r < len(s) and l < len(t):
            if s[r] == t[l]:
                fi+=s[r]
                r+=1
            l+=1

        if fi == s:
            return True
        else:
            return False 


            #optimized Version
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         r = 0
#         l = 0

#         while r < len(s) and l < len(t):
#             if s[r] == t[l]:
#                 r += 1
#             l += 1

#         return r == len(s)

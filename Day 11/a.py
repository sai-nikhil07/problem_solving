#https://leetcode.com/problems/check-if-all-as-appears-before-all-bs

class Solution:
    def checkString(self, s: str) -> bool:
        
        return s == "".join(sorted(s))
        
        # # OR
        
        # #return "ba" not in s
        
        # #or 
        
        # class Solution:
        #     def checkString(self, s: str) -> bool:
        
        # seen_b = False
        
        # for ch in s:
        #     if ch == 'b':
        #         seen_b = True
        #     elif ch == 'a' and seen_b:
        #         return False
                
        # return True

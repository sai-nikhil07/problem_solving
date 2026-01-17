#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1= ""
        for ch in s:
            if ch.isalnum():
                s1+=ch

        final=s1.lower()        
        l=len(final)

        for i in range(len(final)):
            if final[i] != final[l-1]:
                return False
            l-= 1    
        return True


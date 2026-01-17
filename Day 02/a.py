#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        st = [] #( ) [
        map= {')': '(', '}': '{', ']': '['}

        for ch in s: # ex( ) [   { }
            if ch in map: # ] not there
                if not st or st[-1] != map[ch]: #true
                    return False #returns false
                st.pop()
            else:
                st.append(ch)

        return not st

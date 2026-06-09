# https://leetcode.com/problems/find-words-containing-character/
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        l = []

        for i , v in enumerate( words):
            
            if x in v:
                l.append(index(i))

        return l 

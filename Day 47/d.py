#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/ 
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_w = 0
        
        for i in sentences:
         
            word = len(i.split())
          
            if word > max_w:
                max_w = word
                
        return max_w

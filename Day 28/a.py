# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        fl=0
        tr=0
        for i in range(len(word)):
            
            if word[i].isupper()==False:
                fl+=1
            else:
                tr+=1

        if len(word)==fl or len(word)==tr:
            return True
        if tr == 1 and word[0].isupper():
            return True
        else:
            return False

        # python way
        return (
            word.isupper() or
            word.islower() or
            word.istitle()
        )

        #interview way

        # case 1: first letter lowercase → all must be lowercase
        if word[0].islower():
            return word.islower()
        
        # case 2: first letter uppercase
        else:
            return word[1:].islower() or word[1:].isupper()

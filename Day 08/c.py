#https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

        a = ord(coordinate1[0])
        b = int (coordinate1[1]) 
        g = a + b 
        
        c = ord(coordinate2[0])
        d = int (coordinate2[1])
        f = c + d
        
        if g%2==f%2:
            return True
        else:
            return False

                #or

       #return ((ord(c1[0]) + int(c1[1])) & 1) == ((ord(c2[0]) + int(c2[1])) & 1)
 

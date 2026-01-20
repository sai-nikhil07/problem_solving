#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        val={

            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            
        }
        total = 0
        
        for i in range(len(s)): #3   5
            if i + 1 < len(s) and val[s[i]] < val[s[i + 1]]: # 2 and s[1] < s[5] ,  2 <5 and 
                total -= val[s[i]] # 0-1                        # L50 < v5
            else:
                total += val[s[i]] # 0 + 50
        
        return total

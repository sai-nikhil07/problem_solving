#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #prices = [7,1,5,3,6,4]
        # op 5
          
        mini = float('inf') # 7 
        maxx = 0      # 

        for i in prices:
            mini = min(mini , i) #7 1 1 1 1 i<mini
            profit = i - mini #0 -6 4 2 5 profit=i
            maxx = max(maxx, profit) # 0  0 4 4 5 
            
        return maxx

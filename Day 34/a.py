# https://leetcode.com/problems/binary-gap

class Solution:
    def binaryGap(self, n: int) -> int:
  

        n=bin(n)[2:]
        dis=[]
        gap=[0]

        for i,v in enumerate (n):

            if v=="1":
                dis.append(i)
        for i in range(len(dis)-1):
            gap.append(dis[i+1]-dis[i])
          
        # more efficient 
        return max(gap)
      n=bin(n)[2:]
        prev = None
        max_gap = 0

        for i, v in enumerate(n):
            if v == "1":
                if prev is not None:
                    gap = i - prev
                    max_gap = max(max_gap, gap)
                prev = i

        return max_gap

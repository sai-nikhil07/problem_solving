# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # for i in range (1, n+1):
        #     if isBadVersion(i):   not working
        #         return i

        l,r=0,n

        while l<r:
            mid=(l+r)//2
        
            if isBadVersion(mid):
                r=mid
            else :
                l=mid+1
        return l

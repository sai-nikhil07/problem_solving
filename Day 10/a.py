#https://leetcode.com/problems/minimum-absolute-difference/
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = float('inf')
        res = []

        #firstpass find minimum difference
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            min_diff = min(min_diff, diff)


        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                res.append([arr[i], arr[i+1]])

        return res

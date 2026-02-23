# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = len(nums) + 1   # start with impossible large length

        for right in range(len(nums)):
            current_sum += nums[right]

            # try to shrink the window while sum is enough
            while current_sum >= target:
                window_length = right - left + 1
                if window_length < min_length:
                    min_length = window_length

                current_sum -= nums[left]
                left += 1

        # if we never found a valid subarray
        if min_length == len(nums) + 1:
            return 0
        else:
            return min_length

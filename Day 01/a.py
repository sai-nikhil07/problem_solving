# https://leetcode.com/problems/longest-common-prefix/submissions/1886644384/?roomId=lwCIGB
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        shortest = min(strs, key=len)
        l=len(shortest) #3
        for i in range(l):
            for s in strs:
                if s[i] != shortest[i]:
                    return shortest[:i]

        return shortest


# # -------- driver code (THIS PART IS IMPORTANT) --------
# if __name__ == "__main__":
#     sol = Solution()

#     # Test cases
#     print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
#     print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # ""
#     print(sol.longestCommonPrefix(["interview", "internet", "internal"]))  # inte

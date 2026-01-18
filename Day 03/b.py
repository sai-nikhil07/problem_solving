class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #can't be anagrams
        if len(s) != len(t):
            return False

        count = {}

        #  count chars
        for ch in s:
            count[ch] = count.get(ch, 0) + 1


        #  subtract counts using t
        for ch in t:
            if ch not in count:
                return False

            count[ch] -= 1


            if count[ch] < 0:
                return False

        #all counts matched
        return True

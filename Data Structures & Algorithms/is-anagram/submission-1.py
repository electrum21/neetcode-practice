class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettercount = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char not in lettercount:
                lettercount[char] = 1
            else:
                lettercount[char] += 1
        for char in t:
            if char not in lettercount or lettercount[char] == 0:
                return False
            else:
                lettercount[char] -= 1
        return True
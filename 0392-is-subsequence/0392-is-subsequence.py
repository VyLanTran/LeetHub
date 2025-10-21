class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            a, b = s[i], t[j]
            if a == b:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)
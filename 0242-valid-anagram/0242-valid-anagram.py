class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            index = ord(c) - ord('a')
            count[index] -= 1
            if count[index] < 0:
                return False
        return True
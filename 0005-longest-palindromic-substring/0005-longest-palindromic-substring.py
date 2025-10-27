class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        n = len(s)

        def expand(l, r):
            while l - 1 >= 0 and r + 1 < n and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            return l, r

        for i in range(n - 1):
            l, r = expand(i, i)
            if r - l > right - left:
                left, right = l, r
            if s[i] == s[i + 1]:
                l, r = expand(i, i + 1)
                if r - l > right - left:
                    left, right = l, r
        
        return s[left:(right + 1)]
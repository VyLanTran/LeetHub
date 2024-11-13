class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        0123
        cbbd
        '''
        n = len(s)
        
        def helper(i):
            odd = s[i]
            even = ""
            
            for j in range(1, n):
                if i - j < 0 or i + j >= n:
                    break
                if s[i - j] != s[i + j]:
                    break
                odd = s[i - j] + odd + s[i + j]
            
            j = i + 1
            if j < n:
                for k in range(n):
                    if i - k < 0 or j + k >= n:
                        break
                    if s[i - k] != s[j + k]:
                        break
                    even = s[i - k] + even + s[j + k]
            return odd if len(odd) >= len(even) else even
        
        res = ""
        for i in range(n):
            candidate = helper(i)
            res = candidate if len(candidate) > len(res) else res
        return res
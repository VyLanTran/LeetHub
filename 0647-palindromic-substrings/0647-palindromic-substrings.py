class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        n = len(s)

        def extend_palindrome(a, b):
            i, j = a, b
            while i - 1 >= 0 and j + 1 < n and s[i - 1] == s[j + 1]:
                i -= 1
                j += 1
            return a - i + 1

        res = 0
        for i in range(n):
            res += extend_palindrome(i, i)
            if i + 1 < n and s[i] == s[i + 1]:
                res += extend_palindrome(i, i + 1)
        return res

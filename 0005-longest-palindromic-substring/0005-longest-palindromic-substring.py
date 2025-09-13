class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        0 + 1 + 2 + ... + 2 + 0 + 1
        0 -> n/2

        Time: O(n^2)
        Space: O(1)
        '''
        s_len = len(s)
        best_start, best_end = 0, -1

        def expand_palindrome(start, end):
            while start - 1 >= 0 and end + 1 < s_len and s[start - 1] == s[end + 1]:
                start -= 1
                end += 1
            return start, end

        for i in range(s_len):
            start, end = expand_palindrome(i, i)
            if end - start > best_end - best_start:
                best_start, best_end = start, end
            if i < s_len - 1 and s[i] == s[i + 1]:
                start, end = expand_palindrome(i, i + 1)
            if end - start > best_end - best_start:
                best_start, best_end = start, end
        
        return s[best_start:(best_end + 1)]


        

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        count = [0] * 128
        res = 0
        
        for right in range(n):
            c = s[right]
            count[ord(c)] += 1
            while count[ord(c)] > 1:
                count[ord(s[left])] -= 1
                left += 1
            res = max(res, right - left + 1)
            
        return res
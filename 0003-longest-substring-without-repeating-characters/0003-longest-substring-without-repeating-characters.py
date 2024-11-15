class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        01234567
        abcabcbb
        RRRRR
        LLL
        
        maxLen = 3
        frequency = {
            a: 1,
            b: 2,
            c: 1
        }
        
        Time: O(n) where n = len(s)
        Space: O(n)
        
        
        '''
        
        n = len(s)
        left = 0
        frequency = defaultdict(int)
        maxLen = 0
        
        for right in range(n):
            char = s[right]
            frequency[char] += 1
            while frequency[char] > 1:
                removedChar = s[left]
                frequency[removedChar] -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
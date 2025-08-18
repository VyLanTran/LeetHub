class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        '''
        01234567
        bcbbbcba
        jjjj
        ii
        
        {
            b: 1, 2, 3, 2
            c: 1
        }

        max = 3
        '''

        freq = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]
            freq[char] += 1
            
            while left <= right and freq[char] > 2:
                freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len


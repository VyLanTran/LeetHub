class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        '''
        use reasoning to solve the problem, don't need a proper algo at this
        point, just explain step by step how you would solve this problem
        as a human
        
        intuition?
        edge case?
        '''

        freq = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]
            freq[char] += 1
            
            while freq[char] > 2:
                freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len


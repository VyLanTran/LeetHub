class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        s = "ABAB", k = 2
        
        AAAA => return 4
        
        s = "AABABBA", k = 1
        
        k = 1
        ABBABBA => 5
        
        '''
        
        freq = [0] * 128
        maxF = 0
        left = 0
        n = len(s)
        res = 0
        for right in range(n):
            char = s[right]
            i = ord(char)
            freq[i] += 1
            maxF = max(maxF, freq[i])
            if right - left + 1 > maxF:
                while right - left + 1 - maxF > k:
                    leftChar = s[left]
                    freq[ord(leftChar)] -= 1
                    maxF = max(freq)
                    left += 1
            res = max(res, right - left + 1)
        return res
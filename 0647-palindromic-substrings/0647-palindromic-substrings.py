class Solution:
    def countSubstrings(self, s: str) -> int:        
        def countOddLen(s):
            count = 0
            for i in range(len(s)):
                for k in range(0, len(s)):
                    if i - k < 0 or i + k >= len(s) or s[i - k] != s[i+ k]:
                        break
                    count += 1
            return count
        
        def countEvenLen(s):
            count = 0
            for i in range(1, len(s)):
                center = i - 0.5
                dist = 0.5
                while center - dist >= 0 and center + dist < len(s):
                    if s[int(center - dist)] == s[int(center + dist)]:
                        count += 1
                        dist += 1
                    else:
                        break
            return count
        
        return countOddLen(s) + countEvenLen(s)
                        

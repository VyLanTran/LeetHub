class Solution:
    def countSubstrings(self, s: str) -> int:     
        
        def helper(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        res = 0
        for mid in range(len(s)):
            res += helper(s, mid, mid)
            res += helper(s, mid, mid + 1)
        
        return res
                
        
#         def countOddLen(s):
#             count = 0
#             for i in range(len(s)):
#                 for k in range(0, len(s)):
#                     if i - k < 0 or i + k >= len(s) or s[i - k] != s[i+ k]:
#                         break
#                     count += 1
#             return count
        
#         def countEvenLen(s):
#             count = 0
#             for i in range(1, len(s)):
#                 center = i - 0.5
#                 dist = 0.5
#                 while center - dist >= 0 and center + dist < len(s):
#                     if s[int(center - dist)] == s[int(center + dist)]:
#                         count += 1
#                         dist += 1
#                     else:
#                         break
#             return count
        
#         return countOddLen(s) + countEvenLen(s)
                        

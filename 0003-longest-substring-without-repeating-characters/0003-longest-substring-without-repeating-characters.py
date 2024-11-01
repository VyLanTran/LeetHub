class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            char = s[right]
            count[char] += 1
            while count[char] > 1:
                leftChar = s[left]
                count[leftChar] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
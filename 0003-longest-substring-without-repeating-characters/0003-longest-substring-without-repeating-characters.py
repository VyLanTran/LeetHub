class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        res = 0
        count = defaultdict(int)
        left = 0

        for right, char in enumerate(s):
            count[char] += 1
            while count[char] > 1:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
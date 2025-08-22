class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        char_freq = defaultdict(int)

        for right in range(len(s)):
            char = s[right]
            char_freq[char] += 1

            while char_freq[char] > 1:
                removed_char = s[left]
                char_freq[removed_char] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        return max_len
            


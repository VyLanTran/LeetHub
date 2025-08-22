class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        '''
        {
            b: 1 -> 2 -> 3 -> 2 -> 3 -> 2
            c: 1 -> 0 -> 1
            a: 1
        }

        max_len = 3 (bcb) -> 4 (bbca)
        '''

        max_len = 0
        char_freq = defaultdict(int)
        left = 0

        for right in range(len(s)):
            char = s[right]
            char_freq[char] += 1

            while char_freq[char] > 2:
                # solve the problem
                removed_char = s[left]
                char_freq[removed_char] -= 1
                left += 1

            # we have a valid substring at this point
            max_len = max(max_len, right - left + 1)

        return max_len

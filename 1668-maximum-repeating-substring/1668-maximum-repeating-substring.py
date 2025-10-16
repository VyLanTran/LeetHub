class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        left, right = 0, n // m
        max_len = 0

        while left <= right:
            mid = left + (right - left) // 2
            if (word * mid) in sequence:
                max_len = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return max_len
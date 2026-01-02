class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def merge(word1, word2):
            m = min(len(word1), len(word2))
            i = 0
            while i < m:
                if word1[i] != word2[i]:
                    break
                i += 1
            return word1[:i]

        def divide(left, right):
            if left == right:
                return strs[left]
            mid = left + (right - left) // 2
            left_prefix = divide(left, mid)
            right_prefix = divide(mid + 1, right)
            return merge(left_prefix, right_prefix)

        return divide(0, len(strs) - 1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        word1 = strs[0]
        res = word1

        for i in range(1, n):
            word2 = strs[i]
            j = 0
            while j < min(len(word1), len(word2)):
                if word1[j] == word2[j]:
                    j += 1
                else:
                    break
            res = word1[:j]
            word1 = res

        return res


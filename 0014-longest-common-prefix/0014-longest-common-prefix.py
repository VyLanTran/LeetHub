class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        n = len(strs)
        k = max len of a string
        Time: O(kn)
        '''

        n = len(strs)
        prefix = strs[0]
        pointer = len(prefix) - 1

        for i in range(1, n):
            s = strs[i]
            i, j = 0, 0
            while i <= pointer and j < len(s) and prefix[i] == s[j]:
                i += 1
                j += 1
            pointer = i - 1

        return prefix[:(pointer + 1)]

        
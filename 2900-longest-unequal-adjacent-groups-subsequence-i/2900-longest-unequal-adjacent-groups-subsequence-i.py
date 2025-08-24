class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        '''
        Time: O(n)
        Space: O(1)
        '''
        cur = groups[0]
        res = [words[0]]
        i = 1

        while i < len(groups):
            if groups[i] != cur:
                res.append(words[i])
                cur = groups[i]
            i += 1

        return res



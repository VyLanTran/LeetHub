class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        '''
        2 similar strings -> return both of them

        Approach 1:

        n = number of words
        m = max length of a word
        Time: O(m^2n^2)
        Space: O(1)
        '''

        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if j != i and words[i] in words[j]:
                    res.append(words[i])
                    break

        return res
class Solution:
    def possibleStringCount(self, word: str) -> int:
        '''
        Time: O(n)
        Space: O(1)
        
        '''

        res = 0
        left, right = 0, 0

        while right < len(word):
            while right < len(word) and word[left] == word[right]:
                right += 1
            res += right - left - 1
            left = right
        
        return res + 1


class Solution:
    def possibleStringCount(self, word: str) -> int:
        '''
        0123456
        abbcccc
        rrrrrrrr
        ll l

        res = 0, 1, 4
        
        '''

        res = 0
        left, right = 0, 0

        while right < len(word):
            while right < len(word) and word[left] == word[right]:
                right += 1
            if right - left > 1:
                res += right - left - 1
            left = right
        
        return res + 1


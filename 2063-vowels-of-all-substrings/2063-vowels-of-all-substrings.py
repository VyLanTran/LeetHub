class Solution:
    def countVowels(self, word: str) -> int:
        '''
        Time: O(n)
        Space: O(1)

        a substring that contains * is any string that 
            start <= i => i + 1 options
            end >= i => n -i options
        => (index + 1) * (n - index)
        '''

        res = 0
        n = len(word)

        for i, char in enumerate(word):
            if char in "aeiou":
                res += (i + 1) * (n - i)
        
        return res
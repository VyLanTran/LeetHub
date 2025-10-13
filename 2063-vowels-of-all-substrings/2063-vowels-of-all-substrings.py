class Solution:
    def countVowels(self, word: str) -> int:
        '''
        len = n 
        012
        aba

        a: contribute to 1 * 3 = 3
        a: 3 * 1 = 3

        0123456
        xxxx*xx
        
        index of * is 4
        a substring that contains * is any string that 
            start <= 4 => 5 options
            end >= 4 => 3 options
        => 15 
        => (index + 1) * (n - index)

        
        '''

        res = 0
        n = len(word)

        for i, char in enumerate(word):
            if char in "aeiou":
                res += (i + 1) * (n - i)
        
        return res
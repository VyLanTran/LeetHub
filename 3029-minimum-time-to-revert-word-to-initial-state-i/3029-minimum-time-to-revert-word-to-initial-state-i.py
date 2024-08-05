class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        '''
        0 1 2 3 4 5 6 7
        a b c b a b c d
        
        n = 8
        res = 1
        i = 2
        
        
        '''
        
        n = len(word)
        res = 1
        i = k
        
        while i < n:
            size = n - i
            if word[i:] == word[0:size]:
                return res
            i += k
            res += 1
        return res
                
        
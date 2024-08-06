class Solution:
    def minimumLength(self, s: str) -> int:
        '''
        0 1 2 3 4 5 6 7 8
        a a b c c a b b a
        i i i j _ j j j j                 
        
        aabaa
        0123
        aaaa
        iiij
        
        i = 3, j = 2
        
        aaaaba
        iiii.j
        '''
        
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            while i + 1 < j and s[i + 1] == s[i]:
                i += 1
            while j - 1 > i and s[j - 1] == s[j]:
                j -= 1
            i += 1
            j -= 1
        return j - i + 1
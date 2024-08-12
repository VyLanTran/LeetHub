class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        '''
        01234567
        coaching
        iiiiiiiii
        
        012345
        coding
        jjj
        '''
        sLen, tLen = len(s), len(t)
        i, j = 0, 0
        while i < sLen and j < tLen:
            target = t[j]
            while i < sLen:
                if s[i] == target:
                    j += 1
                    i += 1
                    break
                i += 1
        return tLen - j
            
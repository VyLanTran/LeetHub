class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        '''
        012345
        abbaba
        jjjjj
        i
        
        set = a, ab, b, abb, bb, abba, bba, ba, abbab, bbab, bab, 
        maxLen = ab
        
        substring end with i
        0: a
        1: ab, b
        2: abb, bb, b
        '''
        
        visitedSubstrings = set()
        globalString = ""
        maxString = ""
        maxLen = 0
        
        for j in range(len(s)):
            globalString += s[j]
            for i in range(-1, j):
                localString = s[i+1:j+1]
                if localString in visitedSubstrings and len(localString) > len(maxString):
                    maxString = localString
                    maxLen = len(maxString)
                visitedSubstrings.add(localString)
                
        return maxLen
                
                
            
            
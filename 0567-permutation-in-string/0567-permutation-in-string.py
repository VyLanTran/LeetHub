class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def countFreq(s):
            freq = dict()
            for c in s:
                freq[c] = freq.get(c, 0) + 1
            return freq
        
        freq = countFreq(s1)
        
        i = 0
        for j in range(len(s2)):
            c = s2[j]
            freq[c] = freq.get(c, 0) - 1
            while freq[c] < 0:
                freq[s2[i]] += 1
                i += 1
            if j - i + 1 == len(s1):
                return True
        return False
        
            
            

       
        
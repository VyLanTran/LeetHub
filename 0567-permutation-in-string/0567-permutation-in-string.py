class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def countFreq(word):
            map = dict()
            for c in word:
                map[c] = 1 + (map[c] if c in map else 0)
            return map
        
        map1 = countFreq(s1)
        map2 = dict()
        i = 0
        for j in range(len(s2)):
            c = s2[j]
            map2[c] = 1 + (map2[c] if c in map2 else 0)
            freq = map1[c] if c in map1 else 0
            while map2[c] > freq:
                map2[s2[i]] -= 1
                i += 1
            if j - i + 1 == len(s1):
                return True
        return False
            
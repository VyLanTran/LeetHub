class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        aIndex = []
        bIndex = []
        res = []
        
        for i in range(len(s) - len(a) + 1):
            if s[i: (i + len(a))] == a:
                aIndex.append(i)
                
        for i in range(len(s) - len(b) + 1):
            if s[i: (i + len(b))] == b:
                bIndex.append(i)
                
        for i in aIndex:
            for j in bIndex:
                if abs(i - j) <= k:
                    res.append(i)
                    break
                
        return res
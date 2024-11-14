class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def countFromMiddle(i):
            oddCount, evenCount = 0, 0
            
            for j in range(n):
                if i - j < 0 or i + j >= n or s[i - j] != s[i + j]:
                    break
                oddCount += 1
                
            j = i + 1
            if j < n:
                for k in range(n):
                    if i - k < 0 or j + k >= n or s[i - k] != s[j + k]:
                        break
                    evenCount += 1
                    
            return oddCount + evenCount
        
        res = 0
        for i in range(n):
            res += countFromMiddle(i)
        return res
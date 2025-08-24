class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        num_fill = (k - (n % k)) % k
        s += fill * num_fill
        res = []

        for i in range(0, len(s), k):
            res.append(s[i : (i + k)])
        
        return res


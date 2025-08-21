class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        return max(freq for freq in counter.values() if freq % 2 == 1) - min(freq for freq in counter.values() if freq % 2 == 0)
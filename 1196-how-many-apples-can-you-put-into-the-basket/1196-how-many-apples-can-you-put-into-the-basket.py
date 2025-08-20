class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        total_weight = 0

        for i, w in enumerate(weight):
            if total_weight + w > 5000:
                return i
            total_weight += w

        return len(weight)
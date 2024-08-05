class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        res, turn = 0, 0
        for i in range(k):
            res += max(happiness[i] - turn, 0)
            turn += 1
        return res
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freq = dict()
        for num in target:
            freq[num] = freq.get(num, 0) + 1
        for num in arr:
            if num not in freq or freq[num] == 0:
                return False
            freq[num] -= 1
        return True
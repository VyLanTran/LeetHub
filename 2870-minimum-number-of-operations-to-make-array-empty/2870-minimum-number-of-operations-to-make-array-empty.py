class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        res = 0
        for val in freq.values():
            if val == 1:
                return -1
            if val % 3 == 0:
                res += val // 3
            elif val % 3 == 1:
                res += (val - 4) // 3 + 2
            else:
                res += (val - 2) // 3 + 1
        return res
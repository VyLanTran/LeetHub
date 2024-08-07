class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        negatives = set()
        for num in nums:
            if num < 0:
                negatives.add(num)
        res = -1
        for num in nums:
            if num > 0 and -num in negatives and num > res:
                res = num
        return res
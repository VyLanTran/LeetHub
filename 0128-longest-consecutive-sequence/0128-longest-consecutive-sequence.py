class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in num_set:
            if num - 1 not in num_set:
                count = 1
                cur = num 
                while cur + 1 in num_set:
                    count += 1
                    cur += 1
                res = max(res, count)
        return res
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        max_len = 1
        nums = set(nums)

        for num in nums:
            # if this num is the beginning of a sequence
            if num - 1 not in nums:
                cur_len = 1
                while num + 1 in nums:
                    cur_len += 1
                    num += 1
                max_len = max(max_len, cur_len)
        return max_len
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        pre_count, count = 0, 1
        n = len(nums)
        i = 0
        max_len = 0

        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] > nums[j]:
                count += 1
                j += 1
            max_len = max(max_len, min(pre_count, count))
            max_len = max(max_len, count // 2)
            i = j + 1
            pre_count, count = count, 1

        return max_len

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''

        nums_len = len(nums)
        max_global_sum = nums[0]
        max_local_sum = 0

        for i, num in enumerate(nums):
            max_local_sum = max(max_local_sum + num, num)
            max_global_sum = max(max_global_sum, max_local_sum)

        return max_global_sum


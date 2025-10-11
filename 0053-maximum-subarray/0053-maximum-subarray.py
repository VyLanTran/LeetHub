class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
         0,1, 2,3, 4,5,6, 7,8
        -2,1,-3,4,-1,2,1,-5,4

        max_global_sum
        for each index i, want to find
            sum[i] = max sum of a subarray that ends with nums[i]
            update max_sum

        sum[i]
            sum[i - 1] + nums[i]
            nums[i]
        keep track of prevoius max_local_sum = sum[i - 1]
        '''

        nums_len = len(nums)
        max_global_sum = nums[0]
        max_local_sum = 0

        for i, num in enumerate(nums):
            max_local_sum = max(max_local_sum + num, num)
            max_global_sum = max(max_global_sum, max_local_sum)

        return max_global_sum


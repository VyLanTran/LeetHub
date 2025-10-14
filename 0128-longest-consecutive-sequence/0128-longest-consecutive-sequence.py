class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        100,4,200,1,3,2
          1,
        '''

        unique_nums = set(nums)
        n = len(nums)
        dp = {}
        max_len = 0

        def f(num):
            if num in dp:
                return dp[num]
            if num - 1 not in unique_nums:
                dp[num] = 1
                return 1
            res = 1 + f(num - 1)
            dp[num] = res
            return res

        for num in unique_nums:
            max_len = max(max_len, f(num))

        return max_len

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''

        nums = set(nums)
        dp = {}
        max_len = 1

        def f(num):
            if sqrt(num) not in nums:
                dp[num] = 1
                return 1
            if num in dp:
                return dp[num]
            res = 1 + f(int(sqrt(num)))
            dp[num] = res
            return res

        for num in nums:
            max_len = max(max_len, f(num))
        
        return -1 if max_len == 1 else max_len
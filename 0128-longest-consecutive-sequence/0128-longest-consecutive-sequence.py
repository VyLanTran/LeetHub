class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        dp = dict()
        longestStreak = 0
        
        def rec(num):
            if num in dp:
                return dp[num]
            res = 1 + (rec(num - 1) if num - 1 in uniqueNums else 0)
            dp[num] = res
            return res
        
        for num in nums:
            longestStreak = max(longestStreak, rec(num))
        return longestStreak
        
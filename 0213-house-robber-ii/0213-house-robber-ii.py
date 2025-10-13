class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)

        solution for nums[:] can be
            dp[-2] -> same as for nums[:n-1], or
            dp[-1] that is != dp[-2] -> nums[-1] is used
                -> same as for nums[1:]

        But is it possible for nums[:n-1] same as nums[1:]
        [_] -> n = 1

        Thus, we want to solve for 2 problems
            nums[:n-1] and nums[1:] 
        for each problem, return dp[end]
        then return the max of 2 solutions
        ''' 

        def linear_rob(start, end):
            n = end - start + 1
            if n == 1:
                return nums[start]
            a, b = nums[start], max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                c = max(b, nums[i] + a)
                a, b = b, c
            return max(a, b)

        n = len(nums)
        if n == 1:
            return nums[0]
        max_without_last_house = linear_rob(0, n - 2)
        max_without_first_house = linear_rob(1, n - 1)
        return max(max_without_last_house, max_without_first_house)

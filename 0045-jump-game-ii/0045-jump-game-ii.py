class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Time: O(n^2)
        Space: O(n)
        ---
        f(i) = min number of jumps to go from index 0 to index i
            if i == 0:
                return 0
            if i in dp:
                return
            res = inf
            for j in range(0, i):
                largest_steps = nums[j]
                distance = i - j
                if distance <= largest_steps:
                    res = min(res, 1 + f(j))
            put res into dp
            return res
        '''

        # n = len(nums)
        # dp = [float('inf')] * n
        # dp[0] = 0

        # for i in range(1, n):
        #     for j in range(i):
        #         if i - j <= nums[j]:
        #             dp[i] = min(dp[i], 1 + dp[j])
        # return dp[-1]

        '''
        BFS is better because we find the smallest number of steps
        so it's kinda like layers 0 (i=0), 1 (all indices reachable from layer 0 in 1 step), 2, 3, ...

        Time: O(n)
        Space: O(1)
        '''

        n = len(nums)
        l, r = 0, 0
        res = 0

        while r < n - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l, r = r + 1, furthest
            res += 1
        return res
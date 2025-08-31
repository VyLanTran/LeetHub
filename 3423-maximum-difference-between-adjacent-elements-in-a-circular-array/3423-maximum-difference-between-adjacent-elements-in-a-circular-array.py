class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''

        res = 0
        n = len(nums)

        for i in range(n):
            res = max(res, abs(nums[i] - nums[(i + 1) % n]))

        return res
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''

        n = len(nums)
        if n == 1:
            return nums[0]
        a, b = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            c = max(b, a + nums[i])
            a, b = b, c
        
        return max(a, b)

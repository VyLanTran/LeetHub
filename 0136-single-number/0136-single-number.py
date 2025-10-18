class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        If a and b are bits (0 or 1)
        a ^ b = 0 if a == b
              = 1 else

        For numbers
        a ^ 0 = a
        a ^ a = 0

        x1, x1, x2, x2, ..., xn-1, xn-1, xn
          0 ^     0 ^.        0         ^ xn
          0 ^ xn = xn
        '''

        '''
        Time: O(n)
        Space: O(1)
        '''

        res = nums[0]

        for i in range(1, len(nums)):
            res ^= nums[i]

        return res
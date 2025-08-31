class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        '''
        Can't use three sum because array is not sorted, and quadruples must remain index order
        '''

        res = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            res += 1

        return res
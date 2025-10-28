class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        n = len
        For each i (n iterations): 2 options
        Time: O(2^n * n) - deep copy
        Space: O(n) 
        '''

        cur_set = []
        res = []

        def f(i):
            if i < 0:
                res.append(copy.deepcopy(cur_set))
                return
            # skip
            f(i - 1)
            # select
            cur_set.append(nums[i])
            f(i - 1)
            cur_set.pop()

        f(len(nums) - 1)
        return res
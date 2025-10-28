class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        res = []

        0, 1, 2
        1, 2, 3

        arr = [[]]
        f(i = 2)
            # skip
            f(i = 1)
                # skip
                f(i = 0)
                    # skip
                    f(i = -1)
                    # select
                    arr.append(nums[i])
                    f(i = -1)


        f(i)
            if i < 0:
                add a deep copy of arr to res
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
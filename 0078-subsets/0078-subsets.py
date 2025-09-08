class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        0, 1, 2
        1, 2, 3
        deep copy
        f(i = 0, [])
            # skip
            f(i = 1, [])
                f(i = 2, [])
                    f(i = 3, [])
                        res.append(deepcopy(arr))
                        return
                    f(i = 3, [3])
                    arr.pop()
                f(i = 2, [2])

        ''' 

        res = []

        def rec(i, arr):
            if i >= len(nums):
                res.append(deepcopy(arr))
                return
            rec(i + 1, arr)
            arr.append(nums[i])
            rec(i + 1, arr)
            arr.pop()

        rec(0, [])
        return res


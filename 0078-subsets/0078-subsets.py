class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
                i = 0
        i=1                 i=1
    i=2     i=2

        depth = n
        1 + 2 + 4 + 8 + ... + 2^(n-1)
        S = 2^0 + 2^1 + ... + 2^(n-1)
        2S=       2^1 + ... + 2^(n-1) + 2^n
        S = 2^n - 2^0 
        Time: O(n*2^n) - for each subset, it takes O(n) for deepcopy
        Space: O(n) - the temp arr. We don't count the answer as auxiliary space
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

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        n = len(nums)
        nums.sort()
        
        def backtracking(i, arr):
            if i == n:
                res.add(tuple(copy.deepcopy(arr)))
                return
            backtracking(i + 1, arr)
            arr.append(nums[i])
            backtracking(i + 1, arr)
            arr.pop()
            
        backtracking(0, [])
        res_list = []
        for tup in res:
            res_list.append(list(tup))
        return res_list
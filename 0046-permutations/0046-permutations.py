class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        0, 1, 2
        1, 2, 3
           
        f(i = 0, vals = {1, 2, 3}, arr = [])
            f(1, {2, 3}, [1])
                f(2, {3}, [1, 2])
                    f(3, {}, [1, 2, 3]) *
                f(2, {2}, [1, 3])
            f(1, {1, 3}, arr = [2])
        
        '''
        # res = [1, 3, 5]
        # res.insert(2, 2)
        # print(res)
        
        res = []
        n = len(nums)
        
        def backtracking(i, vals, arr):
            if i == n:
                res.append(copy.deepcopy(arr))
                return
            for j in range(len(vals)):
                num = vals.pop(j)
                arr.append(num)
                backtracking(i + 1, vals, arr)
                vals.insert(j, num)
                arr.pop()
                
        backtracking(0, nums, [])
                
        
        return res


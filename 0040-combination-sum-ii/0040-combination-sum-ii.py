class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
         0, 1, 2, 3, 4, 5, 6
        [1, 1, 2, 5, 6, 7, 10], target = 8

        f(i = 0, target = 8)
            f(i = 1, target = 7)
                f(i = 2, target = 6)
                    f(i = 3, target = 4)
                        target - nums[i] < 0 ==> break
                    f(i = 4, target = 1)
                    f(i = 5, target = 0)
                    
        1, 2, 2, 2, 5
        '''

        n = len(candidates)
        res = []
        candidates.sort()
        
        def rec(start, path, target):
            if target == 0:
                res.append(copy.deepcopy(path))
                return
            if start >= n - 1:
                return
            
            for i in range(start + 1, n):
                # if start == -1 and candidates[i] == 5:
                #     print(i, path, target)
                if i > start + 1 and candidates[i] == candidates[i - 1]:
                    continue
                if target < candidates[i]:
                    break
                path.append(candidates[i])
                rec(i, path, target - candidates[i])
                path.pop()
        
        rec(-1, deque(), target)
        return res
                
        
        
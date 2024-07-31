class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        0, 1, 2, 3
        2, 3, 6, 7
        
        [2, 2, 3]
        f(0, 7)
            f(0, 5)
                f(0, 3)
                    f(0, 1)X
                    f(1, 0)
        '''
        
        res = []
        path = []
        
        def rec(i, target):
            if target < 0:
                return
            if target == 0:
                res.append(copy.deepcopy(path))
                return
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                rec(j, target - candidates[j])
                path.pop()
                
        rec(0, target)
        return res
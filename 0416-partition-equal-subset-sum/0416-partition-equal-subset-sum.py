class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        sum odd => False
        each has total = sum // 2
        
        
        0,   1, 2, 3
        [11, 5, 5, 1]
        
        f(i = 0, target = 11)
            f(1, 0)
         
         0, 1, 2, 3
        [6, 2, 8, 4], 10 each
        
        f(0, 10)
            f(1, 4)
                f(2, 2)
                    f(3, 2)
                        f(4, 2) X
                    
                
        '''
        
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        
        memo = {}
        n = len(nums)
        res = False
        
        def rec(i, target):
            if i >= n:
                return target == 0
            if (i, target) in memo:
                return memo[(i, target)]
            # skip
            if (nums[i] <= target and rec(i + 1, target - nums[i])) or rec(i + 1, target):
                memo[(i, target)] = True
                return True
            memo[(i, target)] = False
            return False
        
        
        res =  rec(0, target)
        # print(memo)
        return res
                
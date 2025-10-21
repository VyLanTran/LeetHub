class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        if sum not divisible by 2:
            return False
        target = sum // 2

        f(i, target)
            if target == 0:
                return True
            if in cache
            return f(i - 1, target - num) or f(i - 1, target)

        i: -1 to n - 1 => n + 1
        j: 0 to target => target + 1
        dp: matrix of size n x (target + 1)

        dp[_][0] = True
        dp[0][j] = False for any j != 0
        don't matrix, just 

        i but actual index is i - 1
        prev = [False] * (target + 1) # stand for i = -1
        prev[0] = True

        for i from 0 -> n-1 (inclusively):
            num = nums[i]
            for j in from (target + 1) to 1 (inclu):
                if j - num >= 0:
                    prev[j] = prev[j] or (prev[j - num])


        return prev[-1]
        '''

        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        prev = [False] * (target + 1)
        prev[0] = True

        for i in range(n):
            num = nums[i]
            for j in range(target, 0, -1):
                if j - num >= 0:
                    prev[j] = prev[j] or prev[j - num]

        return prev[-1]
        
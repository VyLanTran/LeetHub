class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        f(i, target) = res for nums[0, i] and target
            if i < 0:
                if target == 0:
                    return 1
                return 0
            num = nums[i]
            f(i - 1, target - num) + f(i - 1, target + num)

        i: -1 to n - 1 (shift right becomes 0 to n) => n + 1
        j: target - sum to target + sum (shift and become 0 to 2*sum)
                    0                   sum-target

        initialize prev (for index = -1)
        prev = [0] * (n + 1)
        prev[sum-target] = 1
        cur[target] = prev[target - num] + prev[target + num]
        '''


        dp = {}

        def f(i, target):
            if i < 0:
                return 1 if target == 0 else 0
            if (i, target) in dp:
                return dp[(i, target)]
            num = nums[i]
            res = f(i - 1, target - num) + f(i - 1, target + num)
            dp[(i, target)] = res
            return res

        return f(len(nums) - 1, target)
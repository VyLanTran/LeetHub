class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        2, 3, 4
        2, 3, 1

        dp[i] = res for number from 1 to i
            = max(i * freq + dp[i - 2], dp[i - 1])

        2, 5, 6
        2, 1, 1
        4, 9, 10
        ans = 10 (2, 2, 6)

        a = 1 * count[1]
        b = max(a, 2 * count[2])
        if max(unique) == 1:
            return a
        if max(unique) == 2:
            return b

        for num in unique_nums:
            if num <= 2:
                continue
            if i - 1 >= 0:
                diff = num - nums[i - 1]
                if diff >= 2:
                    a, b = b, b
            temp = max(b, num + a)
            a, b = b, temp

        2 3 5
        a b

        2 3 4
        a b t
        3 4 5
        b b t
        '''
        
        counter = Counter(nums)
        nums = list(counter.keys())
        nums.sort()

        a = 1 * counter[1]
        b = max(a, 2 * counter[2])
        if max(nums) == 1:
            return a
        if max(nums) == 2:
            return b

        for i, num in enumerate(nums):
            if num <= 2:
                continue
            if i - 1 >= 0:
                diff = num - nums[i - 1]
                if diff >= 2:
                    a = b
            temp = max(b, num * counter[num] + a)
            a, b = b, temp
        
        return b
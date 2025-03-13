class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        '''
        0, 1, 2
        2, 0, 2

        decrement as much as possible
        num -> max(0, num - val)

        min value of k s.t k >= 0

        possibleZeroArray(k): can nums become a zero-array after the first k quries
        0, 1, 2
        2, 0, 2
        1,-1, 1
        0,-2, 0
        0,-5, 0

        0, 1, 2
        2, 0, 2
        0, 0, 0
       -1, 0, 0
       -2, 0, 0
       -2,-3, 3

       -2,-5,-2
        '''
        isAllZeroes = True
        for num in nums:
            if num != 0:
                isAllZeroes = False
                break
        if isAllZeroes:
            return 0

        numsLen = len(nums)

        def possibleZeroArray(k):
            changes = [0] * numsLen
            for i in range(k + 1):
                start, end, val = queries[i]
                changes[start] -= val
                if end + 1 < numsLen:
                    changes[end + 1] += val
            for i in range(numsLen):
                if i - 1 >= 0:
                    changes[i] += changes[i - 1]
                if nums[i] + changes[i] > 0:
                    return False
            return True
        
        left, right = 0, len(queries) - 1
        minK = float('inf')
        
        while left <= right:
            mid = left + (right - left) // 2
            if possibleZeroArray(mid):
                minK = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return -1 if minK == float('inf') else minK + 1



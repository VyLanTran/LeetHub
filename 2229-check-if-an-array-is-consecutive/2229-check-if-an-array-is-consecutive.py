class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        '''
        keep track of min and max and frequency
        if any number occures twice, return false
        if max - min != n - 1, return false
        '''
        visitedNums = set()
        minVal, maxVal = float('inf'), float('-inf')

        for num in nums:
            if num in visitedNums:
                return False
            visitedNums.add(num)
            minVal = min(minVal, num)
            maxVal = max(maxVal, num)
        
        return maxVal - minVal == len(nums) - 1
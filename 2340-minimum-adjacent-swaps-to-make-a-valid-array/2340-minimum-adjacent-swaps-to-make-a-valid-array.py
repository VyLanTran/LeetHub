class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        def findMinMax():
            minVal, maxVal = float('inf'), float('-inf')
            minIndex, maxIndex = 0, 0
            for i in range(n):
                num = nums[i]
                if num < minVal:
                    minVal = num
                    minIndex = i
                if num >= maxVal:
                    # print("before update", num, maxVal)
                    maxVal = num
                    maxIndex = i
            return minIndex, maxIndex
        
        minIndex, maxIndex = findMinMax()
        # print(minIndex, maxIndex)
        res = minIndex + (n - 1 - maxIndex)
        return res - 1 if minIndex > maxIndex else res
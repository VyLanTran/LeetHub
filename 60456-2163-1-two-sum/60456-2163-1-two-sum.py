class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        1. nums = [1, 2], target = 3, return [0, 1]

        {

        }

        
        '''

        valueToIndex = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in valueToIndex:
                return [i, valueToIndex[complement]]
            else:
                valueToIndex[num] = i
        
        return []

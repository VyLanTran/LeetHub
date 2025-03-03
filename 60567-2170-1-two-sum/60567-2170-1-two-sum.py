class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Feb 24
        
        '''

        valueToIndex = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in valueToIndex:
                return [i, valueToIndex[complement]]
            else:
                valueToIndex[num] = i
        
        return []

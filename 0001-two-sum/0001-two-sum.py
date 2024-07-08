class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tuples = [(nums[i], i) for i in range(len(nums))]
        tuples.sort(key = lambda tup:tup[0])
        left, right = 0, len(nums) - 1
        
        while left < right:
            sum = tuples[left][0] + tuples[right][0]
            if sum == target:
                return [tuples[left][1], tuples[right][1]]
            elif sum < target:
                left += 1
            else:
                right -= 1
        
 
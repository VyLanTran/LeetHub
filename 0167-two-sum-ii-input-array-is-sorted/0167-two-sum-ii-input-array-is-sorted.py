class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left += 1
        else:
            right += 1

        0,1,2 ,3
        2,7,11,15

        l = 0
        r = 3, 2, 1
        sum = 17, 13
        '''

        left, right = 0, len(numbers) - 1

        while left < right:
            twoSum = numbers[left] + numbers[right]
            if twoSum == target:
                return [left + 1, right + 1]
            elif twoSum < target:
                left += 1
            else:
                right -= 1

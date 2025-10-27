class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        arr = [(nums[i], i) for i in range(n)]
        arr.sort()

        i, j = 0, n - 1
        while i < j:
            num1, index1 = arr[i]
            num2, index2 = arr[j]
            total = num1 + num2
            if total == target:
                return [index1, index2]
            elif total < target:
                i += 1
            else:
                j -= 1
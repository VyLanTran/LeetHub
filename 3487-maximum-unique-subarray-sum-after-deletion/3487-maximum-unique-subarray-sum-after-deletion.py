class Solution:
    def maxSum(self, nums: List[int]) -> int:
        visited = set()
        total = 0
        max_non_positive = float('-inf')

        for num in nums:
            if num > 0 and num not in visited:
                total += num
                visited.add(num)
            else:
                max_non_positive = max(max_non_positive, num)

        return total if visited else max_non_positive
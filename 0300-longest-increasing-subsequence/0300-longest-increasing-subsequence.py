class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        subsequence = [nums[0]]

        def binary_search(start, end, target):
            left, right = start, end
            res = right
            while left <= right:
                mid = left + (right - left) // 2
                if subsequence[mid] >= target:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return res
        
        for i in range(1, n):
            num = nums[i]
            if num > subsequence[-1]:
                subsequence.append(num)
            else:
                # find the first number in subsequence that >= num
                j = binary_search(0, len(subsequence) - 1, num)
                subsequence[j] = num

        return len(subsequence)
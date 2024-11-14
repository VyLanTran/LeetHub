class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        incr_sequence = []
        
        def findFirstLarger(target):
            left, right = 0, len(incr_sequence) - 1
            res = 0
            while left <= right:
                mid = left + (right - left) // 2
                if incr_sequence[mid] > target:
                    res = mid
                    right = mid - 1
                elif incr_sequence[mid] == target:
                    return mid
                else:
                    left = mid + 1
            return res
        
        for num in nums:
            if len(incr_sequence) == 0 or num > incr_sequence[-1]:
                incr_sequence.append(num)
            else:
                # find first num that is < num
                index = findFirstLarger(num)
                incr_sequence[index] = num
        return len(incr_sequence)
                
        
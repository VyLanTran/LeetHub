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
                    return -1
                else:
                    left = mid + 1
            return res
        
        for num in nums:
            if len(incr_sequence) == 0 or num > incr_sequence[-1]:
                incr_sequence.append(num)
            else:
                # find first num that is < num
                # print("before:", incr_sequence)
                index = findFirstLarger(num)
                if index != -1:
                    incr_sequence[index] = num
        #         print("after:", incr_sequence)
        # print(incr_sequence)
        return len(incr_sequence)
                
        